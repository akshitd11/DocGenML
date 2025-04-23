def get_transfer_operation(self, operation_name):
    return self.get_conn().transferOperations().get(name=operation_name).execute(num_retries=self.num_retries)