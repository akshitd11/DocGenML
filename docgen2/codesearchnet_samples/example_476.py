def rename(self, from_name, to_name):
    conn = self.get_conn()
    return conn.rename(from_name, to_name)