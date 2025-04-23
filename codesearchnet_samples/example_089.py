def export_instance(self, instance, body, project_id=None):
    try:
        response = self.get_conn().instances().export(project=project_id, instance=instance, body=body).execute(num_retries=self.num_retries)
        operation_name = response['name']
        self._wait_for_operation_to_complete(project_id=project_id, operation_name=operation_name)
    except HttpError as ex:
        raise AirflowException('Exporting instance {} failed: {}'.format(instance, ex.content))