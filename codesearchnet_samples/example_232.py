def run_query(self, body):
    conn = self.get_conn()
    resp = conn.projects().runQuery(projectId=self.project_id, body=body).execute(num_retries=self.num_retries)
    return resp['batch']