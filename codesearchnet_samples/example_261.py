def wait(self, operation):
    submitted = _DataProcOperation(self.get_conn(), operation, self.num_retries)
    submitted.wait_for_done()