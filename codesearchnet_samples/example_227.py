def allocate_ids(self, partial_keys):
    conn = self.get_conn()
    resp = conn.projects().allocateIds(projectId=self.project_id, body={'keys': partial_keys}).execute(num_retries=self.num_retries)
    return resp['keys']