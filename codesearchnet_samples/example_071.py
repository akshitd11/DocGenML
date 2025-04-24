def trigger_dag(args):
    log = LoggingMixin().log
    try:
        message = api_client.trigger_dag(dag_id=args.dag_id, run_id=args.run_id, conf=args.conf, execution_date=args.exec_date)
    except IOError as err:
        log.error(err)
        raise AirflowException(err)
    log.info(message)