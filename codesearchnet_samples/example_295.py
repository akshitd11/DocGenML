def dag_run_status(dag_id, execution_date):
    try:
        execution_date = timezone.parse(execution_date)
    except ValueError:
        error_message = 'Given execution date, {}, could not be identified as a date. Example date format: 2015-11-16T14:34:15+00:00'.format(execution_date)
        _log.info(error_message)
        response = jsonify({'error': error_message})
        response.status_code = 400
        return response
    try:
        info = get_dag_run_state(dag_id, execution_date)
    except AirflowException as err:
        _log.info(err)
        response = jsonify(error='{}'.format(err))
        response.status_code = err.status_code
        return response
    return jsonify(info)