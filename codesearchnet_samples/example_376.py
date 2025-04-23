def _wait_for_operation_to_complete(self, project_id, operation_name, zone=None):
    service = self.get_conn()
    while True:
        if zone is None:
            operation_response = self._check_global_operation_status(service, operation_name, project_id)
        else:
            operation_response = self._check_zone_operation_status(service, operation_name, project_id, zone, self.num_retries)
        if operation_response.get('status') == GceOperationStatus.DONE:
            error = operation_response.get('error')
            if error:
                code = operation_response.get('httpErrorStatusCode')
                msg = operation_response.get('httpErrorMessage')
                error_msg = str(error.get('errors'))[1:-1]
                raise AirflowException('{} {}: '.format(code, msg) + error_msg)
            return
        time.sleep(TIME_TO_SLEEP_IN_SECONDS)