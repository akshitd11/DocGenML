def insert_instance_template(self, body, request_id=None, project_id=None):
    response = self.get_conn().instanceTemplates().insert(project=project_id, body=body, requestId=request_id).execute(num_retries=self.num_retries)
    try:
        operation_name = response['name']
    except KeyError:
        raise AirflowException("Wrong response '{}' returned - it should contain 'name' field".format(response))
    self._wait_for_operation_to_complete(project_id=project_id, operation_name=operation_name)