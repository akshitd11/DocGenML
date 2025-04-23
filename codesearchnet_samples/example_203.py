def create_transfer_job(self, body):
    body = self._inject_project_id(body, BODY, PROJECT_ID)
    return self.get_conn().transferJobs().create(body=body).execute(num_retries=self.num_retries)