def list_transfer_operations(self, filter):
    conn = self.get_conn()
    filter = self._inject_project_id(filter, FILTER, FILTER_PROJECT_ID)
    operations = []
    request = conn.transferOperations().list(name=TRANSFER_OPERATIONS, filter=json.dumps(filter))
    while request is not None:
        response = request.execute(num_retries=self.num_retries)
        if OPERATIONS in response:
            operations.extend(response[OPERATIONS])
        request = conn.transferOperations().list_next(previous_request=request, previous_response=response)
    return operations