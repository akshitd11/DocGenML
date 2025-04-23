def _get_job(self, project_id, job_id):
    job_name = 'projects/{}/jobs/{}'.format(project_id, job_id)
    request = self._mlengine.projects().jobs().get(name=job_name)
    while True:
        try:
            return request.execute()
        except HttpError as e:
            if e.resp.status == 429:
                time.sleep(30)
            else:
                self.log.error('Failed to get MLEngine job: {}'.format(e))
                raise