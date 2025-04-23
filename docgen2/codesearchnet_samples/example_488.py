def get_conn(self):
    conn = self.get_connection(self.conn_id)
    service_options = conn.extra_dejson
    return FileService(account_name=conn.login, account_key=conn.password, **service_options)