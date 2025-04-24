def dag_runs(dag_id):
    try:
        state = request.args.get('state')
        dagruns = get_dag_runs(dag_id, state)
    except AirflowException as err:
        _log.info(err)
        response = jsonify(error='{}'.format(err))
        response.status_code = 400
        return response
    return jsonify(dagruns)