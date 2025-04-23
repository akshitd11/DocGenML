def task_info(dag_id, task_id):
    try:
        info = get_task(dag_id, task_id)
    except AirflowException as err:
        _log.info(err)
        response = jsonify(error='{}'.format(err))
        response.status_code = err.status_code
        return response
    fields = {k: str(v) for (k, v) in vars(info).items() if not k.startswith('_')}
    return jsonify(fields)