def set_machine_type(self, zone, resource_id, body, project_id=None):
    response = self._execute_set_machine_type(zone, resource_id, body, project_id)
    try:
        operation_name = response['name']
    except KeyError:
        raise AirflowException("Wrong response '{}' returned - it should contain 'name' field".format(response))
    self._wait_for_operation_to_complete(project_id=project_id, operation_name=operation_name, zone=zone)