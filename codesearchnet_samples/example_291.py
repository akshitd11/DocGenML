def get_dag_code(dag_id):
    try:
        return get_code(dag_id)
    except AirflowException as err:
        _log.info(err)
        response = jsonify(error='{}'.format(err))
        response.status_code = err.status_code
        return response