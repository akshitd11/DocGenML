def create_job(self, project_id, job, use_existing_job_fn=None):
    request = self._mlengine.projects().jobs().create(parent='projects/{}'.format(project_id), body=job)
    job_id = job['jobId']
    try:
        request.execute()
    except HttpError as e:
        if e.resp.status == 409:
            if use_existing_job_fn is not None:
                existing_job = self._get_job(project_id, job_id)
                if not use_existing_job_fn(existing_job):
                    self.log.error('Job with job_id %s already exist, but it does not match our expectation: %s', job_id, existing_job)
                    raise
            self.log.info('Job with job_id %s already exist. Will waiting for it to finish', job_id)
        else:
            self.log.error('Failed to create MLEngine job: {}'.format(e))
            raise
    return self._wait_for_job_done(project_id, job_id)