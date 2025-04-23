def trigger_dag(dag_id):
    data = request.get_json(force=True)
    run_id = None
    if 'run_id' in data:
        run_id = data['run_id']
    conf = None
    if 'conf' in data:
        conf = data['conf']
    execution_date = None
    if 'execution_date' in data and data['execution_date'] is not None:
        execution_date = data['execution_date']
        try:
            execution_date = timezone.parse(execution_date)
        except ValueError:
            error_message = 'Given execution date, {}, could not be identified as a date. Example date format: 2015-11-16T14:34:15+00:00'.format(execution_date)
            _log.info(error_message)
            response = jsonify({'error': error_message})
            response.status_code = 400
            return response
    try:
        dr = trigger.trigger_dag(dag_id, run_id, conf, execution_date)
    except AirflowException as err:
        _log.error(err)
        response = jsonify(error='{}'.format(err))
        response.status_code = err.status_code
        return response
    if getattr(g, 'user', None):
        _log.info('User %s created %s', g.user, dr)
    response = jsonify(message='Created {}'.format(dr))
    return response