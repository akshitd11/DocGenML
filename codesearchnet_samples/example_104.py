def clear_dag_runs():
    session = settings.Session()
    drs = session.query(DagRun).filter(DagRun.dag_id.in_(DAG_IDS)).all()
    for dr in drs:
        logging.info('Deleting DagRun :: {}'.format(dr))
        session.delete(dr)