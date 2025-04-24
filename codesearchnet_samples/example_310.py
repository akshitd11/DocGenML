def find(dag_id=None, run_id=None, execution_date=None, state=None, external_trigger=None, no_backfills=False, session=None):
    DR = DagRun
    qry = session.query(DR)
    if dag_id:
        qry = qry.filter(DR.dag_id == dag_id)
    if run_id:
        qry = qry.filter(DR.run_id == run_id)
    if execution_date:
        if isinstance(execution_date, list):
            qry = qry.filter(DR.execution_date.in_(execution_date))
        else:
            qry = qry.filter(DR.execution_date == execution_date)
    if state:
        qry = qry.filter(DR.state == state)
    if external_trigger is not None:
        qry = qry.filter(DR.external_trigger == external_trigger)
    if no_backfills:
        from airflow.jobs import BackfillJob
        qry = qry.filter(DR.run_id.notlike(BackfillJob.ID_PREFIX + '%'))
    dr = qry.order_by(DR.execution_date).all()
    return dr