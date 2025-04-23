def skip(self, dag_run, execution_date, tasks, session=None):
    if not tasks:
        return
    task_ids = [d.task_id for d in tasks]
    now = timezone.utcnow()
    if dag_run:
        session.query(TaskInstance).filter(TaskInstance.dag_id == dag_run.dag_id, TaskInstance.execution_date == dag_run.execution_date, TaskInstance.task_id.in_(task_ids)).update({TaskInstance.state: State.SKIPPED, TaskInstance.start_date: now, TaskInstance.end_date: now}, synchronize_session=False)
        session.commit()
    else:
        assert execution_date is not None, 'Execution date is None and no dag run'
        self.log.warning('No DAG RUN present this should not happen')
        for task in tasks:
            ti = TaskInstance(task, execution_date=execution_date)
            ti.state = State.SKIPPED
            ti.start_date = now
            ti.end_date = now
            session.merge(ti)
        session.commit()