def patch_instance_group_manager(self, zone, resource_id, body, request_id=None, project_id=None):
    response = self.get_conn().instanceGroupManagers().patch(project=project_id, zone=zone, instanceGroupManager=resource_id, body=body, requestId=request_id).execute(num_retries=self.num_retries)
    try:
        operation_name = response['name']
    except KeyError:
        raise AirflowException("Wrong response '{}' returned - it should contain 'name' field".format(response))
    self._wait_for_operation_to_complete(project_id=project_id, operation_name=operation_name, zone=zone)