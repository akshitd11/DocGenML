def delete_dag(args):
    log = LoggingMixin().log
    if args.yes or input('This will drop all existing records related to the specified DAG. Proceed? (y/n)').upper() == 'Y':
        try:
            message = api_client.delete_dag(dag_id=args.dag_id)
        except IOError as err:
            log.error(err)
            raise AirflowException(err)
        log.info(message)
    else:
        print('Bail.')