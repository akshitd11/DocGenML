def _check_and_change_state_before_execution(self, verbose=True, ignore_all_deps=False, ignore_depends_on_past=False, ignore_task_deps=False, ignore_ti_state=False, mark_success=False, test_mode=False, job_id=None, pool=None, session=None):
    task = self.task
    self.pool = pool or task.pool
    self.test_mode = test_mode
    self.refresh_from_db(session=session, lock_for_update=True)
    self.job_id = job_id
    self.hostname = get_hostname()
    self.operator = task.__class__.__name__
    if not ignore_all_deps and (not ignore_ti_state) and (self.state == State.SUCCESS):
        Stats.incr('previously_succeeded', 1, 1)
    queue_dep_context = DepContext(deps=QUEUE_DEPS, ignore_all_deps=ignore_all_deps, ignore_ti_state=ignore_ti_state, ignore_depends_on_past=ignore_depends_on_past, ignore_task_deps=ignore_task_deps)
    if not self.are_dependencies_met(dep_context=queue_dep_context, session=session, verbose=True):
        session.commit()
        return False
    hr = '\n' + '-' * 80
    self.start_date = timezone.utcnow()
    task_reschedules = TaskReschedule.find_for_task_instance(self, session)
    if task_reschedules:
        self.start_date = task_reschedules[0].start_date
    dep_context = DepContext(deps=RUN_DEPS - QUEUE_DEPS, ignore_all_deps=ignore_all_deps, ignore_depends_on_past=ignore_depends_on_past, ignore_task_deps=ignore_task_deps, ignore_ti_state=ignore_ti_state)
    runnable = self.are_dependencies_met(dep_context=dep_context, session=session, verbose=True)
    if not runnable and (not mark_success):
        self.state = State.NONE
        self.log.warning(hr)
        self.log.warning('FIXME: Rescheduling due to concurrency limits reached at task runtime. Attempt %s of %s. State set to NONE.', self.try_number, self.max_tries + 1)
        self.log.warning(hr)
        self.queued_dttm = timezone.utcnow()
        self.log.info('Queuing into pool %s', self.pool)
        session.merge(self)
        session.commit()
        return False
    if self.state == State.RUNNING:
        self.log.warning('Task Instance already running %s', self)
        session.commit()
        return False
    self.log.info(hr)
    self.log.info('Starting attempt %s of %s', self.try_number, self.max_tries + 1)
    self.log.info(hr)
    self._try_number += 1
    if not test_mode:
        session.add(Log(State.RUNNING, self))
    self.state = State.RUNNING
    self.pid = os.getpid()
    self.end_date = None
    if not test_mode:
        session.merge(self)
    session.commit()
    settings.engine.dispose()
    if verbose:
        if mark_success:
            self.log.info('Marking success for %s on %s', self.task, self.execution_date)
        else:
            self.log.info('Executing %s on %s', self.task, self.execution_date)
    return True