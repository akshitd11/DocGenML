def get_code(dag_id):
    session = settings.Session()
    DM = models.DagModel
    dag = session.query(DM).filter(DM.dag_id == dag_id).first()
    session.close()
    if dag is None:
        error_message = 'Dag id {} not found'.format(dag_id)
        raise DagNotFound(error_message)
    try:
        with wwwutils.open_maybe_zipped(dag.fileloc, 'r') as f:
            code = f.read()
            return code
    except IOError as e:
        error_message = 'Error {} while reading Dag id {} Code'.format(str(e), dag_id)
        raise AirflowException(error_message)