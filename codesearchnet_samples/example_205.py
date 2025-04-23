def list_transfer_job(self, filter):
    conn = self.get_conn()
    filter = self._inject_project_id(filter, FILTER, FILTER_PROJECT_ID)
    request = conn.transferJobs().list(filter=json.dumps(filter))
    jobs = []
    while request is not None:
        response = request.execute(num_retries=self.num_retries)
        jobs.extend(response[TRANSFER_JOBS])
        request = conn.transferJobs().list_next(previous_request=request, previous_response=response)
    return jobs