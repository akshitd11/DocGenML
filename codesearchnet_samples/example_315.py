def update_state(self, session=None):
    dag = self.get_dag()
    tis = self.get_task_instances(session=session)
    self.log.debug('Updating state for %s considering %s task(s)', self, len(tis))
    for ti in list(tis):
        if ti.state == State.REMOVED:
            tis.remove(ti)
        else:
            ti.task = dag.get_task(ti.task_id)
    start_dttm = timezone.utcnow()
    unfinished_tasks = self.get_task_instances(state=State.unfinished(), session=session)
    none_depends_on_past = all((not t.task.depends_on_past for t in unfinished_tasks))
    none_task_concurrency = all((t.task.task_concurrency is None for t in unfinished_tasks))
    if unfinished_tasks and none_depends_on_past and none_task_concurrency:
        no_dependencies_met = True
        for ut in unfinished_tasks:
            old_state = ut.state
            deps_met = ut.are_dependencies_met(dep_context=DepContext(flag_upstream_failed=True, ignore_in_retry_period=True, ignore_in_reschedule_period=True), session=session)
            if deps_met or old_state != ut.current_state(session=session):
                no_dependencies_met = False
                break
    duration = (timezone.utcnow() - start_dttm).total_seconds() * 1000
    Stats.timing('dagrun.dependency-check.{}'.format(self.dag_id), duration)
    root_ids = [t.task_id for t in dag.roots]
    roots = [t for t in tis if t.task_id in root_ids]
    if not unfinished_tasks and any((r.state in (State.FAILED, State.UPSTREAM_FAILED) for r in roots)):
        self.log.info('Marking run %s failed', self)
        self.set_state(State.FAILED)
        dag.handle_callback(self, success=False, reason='task_failure', session=session)
    elif not unfinished_tasks and all((r.state in (State.SUCCESS, State.SKIPPED) for r in roots)):
        self.log.info('Marking run %s successful', self)
        self.set_state(State.SUCCESS)
        dag.handle_callback(self, success=True, reason='success', session=session)
    elif unfinished_tasks and none_depends_on_past and none_task_concurrency and no_dependencies_met:
        self.log.info('Deadlock; marking run %s failed', self)
        self.set_state(State.FAILED)
        dag.handle_callback(self, success=False, reason='all_tasks_deadlocked', session=session)
    else:
        self.set_state(State.RUNNING)
    self._emit_duration_stats_for_finished_state()
    session.merge(self)
    session.commit()
    return self.state