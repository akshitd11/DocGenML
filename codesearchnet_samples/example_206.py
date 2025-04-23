def update_transfer_job(self, job_name, body):
    body = self._inject_project_id(body, BODY, PROJECT_ID)
    return self.get_conn().transferJobs().patch(jobName=job_name, body=body).execute(num_retries=self.num_retries)