def _run_raw_task(self, mark_success=False, test_mode=False, job_id=None, pool=None, session=None):
    task = self.task
    self.pool = pool or task.pool
    self.test_mode = test_mode
    self.refresh_from_db(session=session)
    self.job_id = job_id
    self.hostname = get_hostname()
    self.operator = task.__class__.__name__
    context = {}
    actual_start_date = timezone.utcnow()
    try:
        if not mark_success:
            context = self.get_template_context()
            task_copy = copy.copy(task)
            self.task = task_copy

            def signal_handler(signum, frame):
                self.log.error('Received SIGTERM. Terminating subprocesses.')
                task_copy.on_kill()
                raise AirflowException('Task received SIGTERM signal')
            signal.signal(signal.SIGTERM, signal_handler)
            self.clear_xcom_data()
            start_time = time.time()
            self.render_templates()
            task_copy.pre_execute(context=context)
            result = None
            if task_copy.execution_timeout:
                try:
                    with timeout(int(task_copy.execution_timeout.total_seconds())):
                        result = task_copy.execute(context=context)
                except AirflowTaskTimeout:
                    task_copy.on_kill()
                    raise
            else:
                result = task_copy.execute(context=context)
            if task_copy.do_xcom_push and result is not None:
                self.xcom_push(key=XCOM_RETURN_KEY, value=result)
            task_copy.post_execute(context=context, result=result)
            end_time = time.time()
            duration = end_time - start_time
            Stats.timing('dag.{dag_id}.{task_id}.duration'.format(dag_id=task_copy.dag_id, task_id=task_copy.task_id), duration)
            Stats.incr('operator_successes_{}'.format(self.task.__class__.__name__), 1, 1)
            Stats.incr('ti_successes')
        self.refresh_from_db(lock_for_update=True)
        self.state = State.SUCCESS
    except AirflowSkipException:
        self.refresh_from_db(lock_for_update=True)
        self.state = State.SKIPPED
    except AirflowRescheduleException as reschedule_exception:
        self.refresh_from_db()
        self._handle_reschedule(actual_start_date, reschedule_exception, test_mode, context)
        return
    except AirflowException as e:
        self.refresh_from_db()
        if self.state in {State.SUCCESS, State.FAILED}:
            return
        else:
            self.handle_failure(e, test_mode, context)
            raise
    except (Exception, KeyboardInterrupt) as e:
        self.handle_failure(e, test_mode, context)
        raise
    try:
        if task.on_success_callback:
            task.on_success_callback(context)
    except Exception as e3:
        self.log.error('Failed when executing success callback')
        self.log.exception(e3)
    self.end_date = timezone.utcnow()
    self.set_duration()
    if not test_mode:
        session.add(Log(self.state, self))
        session.merge(self)
    session.commit()