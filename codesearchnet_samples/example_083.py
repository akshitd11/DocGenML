def patch_instance(self, body, instance, project_id=None):
    response = self.get_conn().instances().patch(project=project_id, instance=instance, body=body).execute(num_retries=self.num_retries)
    operation_name = response['name']
    self._wait_for_operation_to_complete(project_id=project_id, operation_name=operation_name)