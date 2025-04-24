def create_new_function(self, location, body, project_id=None):
    response = self.get_conn().projects().locations().functions().create(location=self._full_location(project_id, location), body=body).execute(num_retries=self.num_retries)
    operation_name = response['name']
    self._wait_for_operation_to_complete(operation_name=operation_name)