def delete_pool(name):
    try:
        pool = pool_api.delete_pool(name=name)
    except AirflowException as err:
        _log.error(err)
        response = jsonify(error='{}'.format(err))
        response.status_code = err.status_code
        return response
    else:
        return jsonify(pool.to_json())