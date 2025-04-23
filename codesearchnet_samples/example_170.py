def get_conn(self):
    conn = self.get_connection(self.vertica_conn_id)
    conn_config = {'user': conn.login, 'password': conn.password or '', 'database': conn.schema, 'host': conn.host or 'localhost'}
    if not conn.port:
        conn_config['port'] = 5433
    else:
        conn_config['port'] = int(conn.port)
    conn = connect(**conn_config)
    return conn