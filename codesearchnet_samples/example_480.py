def _set_dag_run_state(dag_id, execution_date, state, session=None):
    DR = DagRun
    dr = session.query(DR).filter(DR.dag_id == dag_id, DR.execution_date == execution_date).one()
    dr.state = state
    if state == State.RUNNING:
        dr.start_date = timezone.utcnow()
        dr.end_date = None
    else:
        dr.end_date = timezone.utcnow()
    session.merge(dr)