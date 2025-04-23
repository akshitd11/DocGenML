def delete_function(self, name):
    response = self.get_conn().projects().locations().functions().delete(name=name).execute(num_retries=self.num_retries)
    operation_name = response['name']
    self._wait_for_operation_to_complete(operation_name=operation_name)