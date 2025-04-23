def update_function(self, name, body, update_mask):
    response = self.get_conn().projects().locations().functions().patch(updateMask=','.join(update_mask), name=name, body=body).execute(num_retries=self.num_retries)
    operation_name = response['name']
    self._wait_for_operation_to_complete(operation_name=operation_name)