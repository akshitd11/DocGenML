def get_task(dag_id, task_id):
    dagbag = DagBag()
    if dag_id not in dagbag.dags:
        error_message = 'Dag id {} not found'.format(dag_id)
        raise DagNotFound(error_message)
    dag = dagbag.get_dag(dag_id)
    if not dag.has_task(task_id):
        error_message = 'Task {} not found in dag {}'.format(task_id, dag_id)
        raise TaskNotFound(error_message)
    return dag.get_task(task_id)