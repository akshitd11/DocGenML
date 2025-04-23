def clear_task_instances(tis, session, activate_dag_runs=True, dag=None):
    job_ids = []
    for ti in tis:
        if ti.state == State.RUNNING:
            if ti.job_id:
                ti.state = State.SHUTDOWN
                job_ids.append(ti.job_id)
        else:
            task_id = ti.task_id
            if dag and dag.has_task(task_id):
                task = dag.get_task(task_id)
                task_retries = task.retries
                ti.max_tries = ti.try_number + task_retries - 1
            else:
                ti.max_tries = max(ti.max_tries, ti.try_number - 1)
            ti.state = State.NONE
            session.merge(ti)
    if job_ids:
        from airflow.jobs import BaseJob as BJ
        for job in session.query(BJ).filter(BJ.id.in_(job_ids)).all():
            job.state = State.SHUTDOWN
    if activate_dag_runs and tis:
        from airflow.models.dagrun import DagRun
        drs = session.query(DagRun).filter(DagRun.dag_id.in_({ti.dag_id for ti in tis}), DagRun.execution_date.in_({ti.execution_date for ti in tis})).all()
        for dr in drs:
            dr.state = State.RUNNING
            dr.start_date = timezone.utcnow()