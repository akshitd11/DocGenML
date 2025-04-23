def _wait_for_operation_to_complete(self, project_id, operation_name):
    service = self.get_conn()
    while True:
        operation_response = service.operations().get(project=project_id, operation=operation_name).execute(num_retries=self.num_retries)
        if operation_response.get('status') == CloudSqlOperationStatus.DONE:
            error = operation_response.get('error')
            if error:
                error_msg = str(error.get('errors'))[1:-1]
                raise AirflowException(error_msg)
            return
        time.sleep(TIME_TO_SLEEP_IN_SECONDS)