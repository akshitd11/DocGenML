def create_pool():
    params = request.get_json(force=True)
    try:
        pool = pool_api.create_pool(**params)
    except AirflowException as err:
        _log.error(err)
        response = jsonify(error='{}'.format(err))
        response.status_code = err.status_code
        return response
    else:
        return jsonify(pool.to_json())