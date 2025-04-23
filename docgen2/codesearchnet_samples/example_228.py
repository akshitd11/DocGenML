def begin_transaction(self):
    conn = self.get_conn()
    resp = conn.projects().beginTransaction(projectId=self.project_id, body={}).execute(num_retries=self.num_retries)
    return resp['transaction']