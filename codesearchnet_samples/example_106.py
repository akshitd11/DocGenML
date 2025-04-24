def set_dags_paused_state(is_paused):
    session = settings.Session()
    dms = session.query(DagModel).filter(DagModel.dag_id.in_(DAG_IDS))
    for dm in dms:
        logging.info('Setting DAG :: {} is_paused={}'.format(dm, is_paused))
        dm.is_paused = is_paused
    session.commit()