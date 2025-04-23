def get_transfer_job(self, job_name, project_id=None):
    return self.get_conn().transferJobs().get(jobName=job_name, projectId=project_id).execute(num_retries=self.num_retries)