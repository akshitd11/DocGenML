def rollback(self, transaction):
    conn = self.get_conn()
    conn.projects().rollback(projectId=self.project_id, body={'transaction': transaction}).execute(num_retries=self.num_retries)