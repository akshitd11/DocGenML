def set_dag_run_state_to_failed(dag, execution_date, commit=False, session=None):
    res = []
    if not dag or not execution_date:
        return res
    if commit:
        _set_dag_run_state(dag.dag_id, execution_date, State.FAILED, session)
    TI = TaskInstance
    task_ids = [task.task_id for task in dag.tasks]
    tis = session.query(TI).filter(TI.dag_id == dag.dag_id, TI.execution_date == execution_date, TI.task_id.in_(task_ids)).filter(TI.state == State.RUNNING)
    task_ids_of_running_tis = [ti.task_id for ti in tis]
    for task in dag.tasks:
        if task.task_id not in task_ids_of_running_tis:
            continue
        task.dag = dag
        new_state = set_state(task=task, execution_date=execution_date, state=State.FAILED, commit=commit)
        res.extend(new_state)
    return res