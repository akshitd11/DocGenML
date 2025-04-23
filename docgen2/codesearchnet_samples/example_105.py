def clear_dag_task_instances():
    session = settings.Session()
    TI = TaskInstance
    tis = session.query(TI).filter(TI.dag_id.in_(DAG_IDS)).all()
    for ti in tis:
        logging.info('Deleting TaskInstance :: {}'.format(ti))
        session.delete(ti)
    session.commit()