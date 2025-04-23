def get_dag_run_state(dag_id, execution_date):
    dagbag = DagBag()
    if dag_id not in dagbag.dags:
        error_message = 'Dag id {} not found'.format(dag_id)
        raise DagNotFound(error_message)
    dag = dagbag.get_dag(dag_id)
    dagrun = dag.get_dagrun(execution_date=execution_date)
    if not dagrun:
        error_message = 'Dag Run for date {} not found in dag {}'.format(execution_date, dag_id)
        raise DagRunNotFound(error_message)
    return {'state': dagrun.get_state()}