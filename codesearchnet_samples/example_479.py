def set_state(task, execution_date, upstream=False, downstream=False, future=False, past=False, state=State.SUCCESS, commit=False, session=None):
    assert timezone.is_localized(execution_date)
    assert task.dag is not None
    dag = task.dag
    latest_execution_date = dag.latest_execution_date
    assert latest_execution_date is not None
    end_date = latest_execution_date if future else execution_date
    if 'start_date' in dag.default_args:
        start_date = dag.default_args['start_date']
    elif dag.start_date:
        start_date = dag.start_date
    else:
        start_date = execution_date
    start_date = execution_date if not past else start_date
    if dag.schedule_interval == '@once':
        dates = [start_date]
    else:
        dates = dag.date_range(start_date=start_date, end_date=end_date)
    task_ids = [task.task_id]
    if downstream:
        relatives = task.get_flat_relatives(upstream=False)
        task_ids += [t.task_id for t in relatives]
    if upstream:
        relatives = task.get_flat_relatives(upstream=True)
        task_ids += [t.task_id for t in relatives]
    confirmed_dates = []
    drs = DagRun.find(dag_id=dag.dag_id, execution_date=dates)
    for dr in drs:
        dr.dag = dag
        dr.verify_integrity()
        confirmed_dates.append(dr.execution_date)
    dags = [dag]
    sub_dag_ids = []
    while len(dags) > 0:
        current_dag = dags.pop()
        for task_id in task_ids:
            if not current_dag.has_task(task_id):
                continue
            current_task = current_dag.get_task(task_id)
            if isinstance(current_task, SubDagOperator):
                drs = _create_dagruns(current_task.subdag, execution_dates=confirmed_dates, state=State.RUNNING, run_id_template=BackfillJob.ID_FORMAT_PREFIX)
                for dr in drs:
                    dr.dag = current_task.subdag
                    dr.verify_integrity()
                    if commit:
                        dr.state = state
                        session.merge(dr)
                dags.append(current_task.subdag)
                sub_dag_ids.append(current_task.subdag.dag_id)
    TI = TaskInstance
    qry_dag = session.query(TI).filter(TI.dag_id == dag.dag_id, TI.execution_date.in_(confirmed_dates), TI.task_id.in_(task_ids)).filter(or_(TI.state.is_(None), TI.state != state))
    if len(sub_dag_ids) > 0:
        qry_sub_dag = session.query(TI).filter(TI.dag_id.in_(sub_dag_ids), TI.execution_date.in_(confirmed_dates)).filter(or_(TI.state.is_(None), TI.state != state))
    if commit:
        tis_altered = qry_dag.with_for_update().all()
        if len(sub_dag_ids) > 0:
            tis_altered += qry_sub_dag.with_for_update().all()
        for ti in tis_altered:
            ti.state = state
    else:
        tis_altered = qry_dag.all()
        if len(sub_dag_ids) > 0:
            tis_altered += qry_sub_dag.all()
    return tis_altered