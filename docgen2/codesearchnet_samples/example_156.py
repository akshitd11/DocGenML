def _wait_for_operation_to_complete(self, operation_name):
    service = self.get_conn()
    while True:
        operation_response = service.operations().get(name=operation_name).execute(num_retries=self.num_retries)
        if operation_response.get('done'):
            response = operation_response.get('response')
            error = operation_response.get('error')
            if error:
                raise AirflowException(str(error))
            return response
        time.sleep(TIME_TO_SLEEP_IN_SECONDS)