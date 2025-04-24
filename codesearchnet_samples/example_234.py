def delete_operation(self, name):
    conn = self.get_conn()
    resp = conn.projects().operations().delete(name=name).execute(num_retries=self.num_retries)
    return resp