def delete_dag(dag_id):
    try:
        count = delete.delete_dag(dag_id)
    except AirflowException as err:
        _log.error(err)
        response = jsonify(error='{}'.format(err))
        response.status_code = err.status_code
        return response
    return jsonify(message='Removed {} record(s)'.format(count), count=count)