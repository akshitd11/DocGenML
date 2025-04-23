def get_conn(self):
    conn = self.get_connection(self.mssql_conn_id)
    conn = pymssql.connect(server=conn.host, user=conn.login, password=conn.password, database=self.schema or conn.schema, port=conn.port)
    return conn