def set_dag_run_state_to_running(dag, execution_date, commit=False, session=None):
    res = []
    if not dag or not execution_date:
        return res
    if commit:
        _set_dag_run_state(dag.dag_id, execution_date, State.RUNNING, session)
    return res