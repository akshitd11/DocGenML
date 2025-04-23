def pause_transfer_operation(self, operation_name):
    self.get_conn().transferOperations().pause(name=operation_name).execute(num_retries=self.num_retries)