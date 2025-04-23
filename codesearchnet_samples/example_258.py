def get_task_instance(dag_id, task_id, execution_date):
    dagbag = DagBag()
    if dag_id not in dagbag.dags:
        error_message = 'Dag id {} not found'.format(dag_id)
        raise DagNotFound(error_message)
    dag = dagbag.get_dag(dag_id)
    if not dag.has_task(task_id):
        error_message = 'Task {} not found in dag {}'.format(task_id, dag_id)
        raise TaskNotFound(error_message)
    dagrun = dag.get_dagrun(execution_date=execution_date)
    if not dagrun:
        error_message = 'Dag Run for date {} not found in dag {}'.format(execution_date, dag_id)
        raise DagRunNotFound(error_message)
    task_instance = dagrun.get_task_instance(task_id)
    if not task_instance:
        error_message = 'Task {} instance for date {} not found'.format(task_id, execution_date)
        raise TaskInstanceNotFound(error_message)
    return task_instance