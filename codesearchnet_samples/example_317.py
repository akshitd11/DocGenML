def get_run(session, dag_id, execution_date):
    qry = session.query(DagRun).filter(DagRun.dag_id == dag_id, DagRun.external_trigger == False, DagRun.execution_date == execution_date)
    return qry.first()