def get_pools():
    try:
        pools = pool_api.get_pools()
    except AirflowException as err:
        _log.error(err)
        response = jsonify(error='{}'.format(err))
        response.status_code = err.status_code
        return response
    else:
        return jsonify([p.to_json() for p in pools])