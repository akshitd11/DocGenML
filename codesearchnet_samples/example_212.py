def resume_transfer_operation(self, operation_name):
    self.get_conn().transferOperations().resume(name=operation_name).execute(num_retries=self.num_retries)