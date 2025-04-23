def start_instance(self, zone, resource_id, project_id=None):
    response = self.get_conn().instances().start(project=project_id, zone=zone, instance=resource_id).execute(num_retries=self.num_retries)
    try:
        operation_name = response['name']
    except KeyError:
        raise AirflowException("Wrong response '{}' returned - it should contain 'name' field".format(response))
    self._wait_for_operation_to_complete(project_id=project_id, operation_name=operation_name, zone=zone)