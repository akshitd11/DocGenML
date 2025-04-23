def _handle_databricks_operator_execution(operator, hook, log, context):
    if operator.do_xcom_push:
        context['ti'].xcom_push(key=XCOM_RUN_ID_KEY, value=operator.run_id)
    log.info('Run submitted with run_id: %s', operator.run_id)
    run_page_url = hook.get_run_page_url(operator.run_id)
    if operator.do_xcom_push:
        context['ti'].xcom_push(key=XCOM_RUN_PAGE_URL_KEY, value=run_page_url)
    log.info('View run status, Spark UI, and logs at %s', run_page_url)
    while True:
        run_state = hook.get_run_state(operator.run_id)
        if run_state.is_terminal:
            if run_state.is_successful:
                log.info('%s completed successfully.', operator.task_id)
                log.info('View run status, Spark UI, and logs at %s', run_page_url)
                return
            else:
                error_message = '{t} failed with terminal state: {s}'.format(t=operator.task_id, s=run_state)
                raise AirflowException(error_message)
        else:
            log.info('%s in run state: %s', operator.task_id, run_state)
            log.info('View run status, Spark UI, and logs at %s', run_page_url)
            log.info('Sleeping for %s seconds.', operator.polling_period_seconds)
            time.sleep(operator.polling_period_seconds)