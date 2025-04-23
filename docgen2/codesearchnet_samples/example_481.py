def set_dag_run_state_to_success(dag, execution_date, commit=False, session=None):
    res = []
    if not dag or not execution_date:
        return res
    if commit:
        _set_dag_run_state(dag.dag_id, execution_date, State.SUCCESS, session)
    for task in dag.tasks:
        task.dag = dag
        new_state = set_state(task=task, execution_date=execution_date, state=State.SUCCESS, commit=commit)
        res.extend(new_state)
    return res