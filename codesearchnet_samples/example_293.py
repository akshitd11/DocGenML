def dag_paused(dag_id, paused):
    DagModel = models.DagModel
    with create_session() as session:
        orm_dag = session.query(DagModel).filter(DagModel.dag_id == dag_id).first()
        if paused == 'true':
            orm_dag.is_paused = True
        else:
            orm_dag.is_paused = False
        session.merge(orm_dag)
        session.commit()
    return jsonify({'response': 'ok'})