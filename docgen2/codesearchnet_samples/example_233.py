def get_operation(self, name):
    conn = self.get_conn()
    resp = conn.projects().operations().get(name=name).execute(num_retries=self.num_retries)
    return resp