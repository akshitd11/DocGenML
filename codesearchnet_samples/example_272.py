def _wait_for_job_done(self, project_id, job_id, interval=30):
    if interval <= 0:
        raise ValueError('Interval must be > 0')
    while True:
        job = self._get_job(project_id, job_id)
        if job['state'] in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
            return job
        time.sleep(interval)