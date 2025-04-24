def task_instance_info(dag_id, execution_date, task_id):
    try:
        execution_date = timezone.parse(execution_date)
    except ValueError:
        error_message = 'Given execution date, {}, could not be identified as a date. Example date format: 2015-11-16T14:34:15+00:00'.format(execution_date)
        _log.info(error_message)
        response = jsonify({'error': error_message})
        response.status_code = 400
        return response
    try:
        info = get_task_instance(dag_id, task_id, execution_date)
    except AirflowException as err:
        _log.info(err)
        response = jsonify(error='{}'.format(err))
        response.status_code = err.status_code
        return response
    fields = {k: str(v) for (k, v) in vars(info).items() if not k.startswith('_')}
    return jsonify(fields)