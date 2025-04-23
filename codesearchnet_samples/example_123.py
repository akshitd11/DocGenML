def get_conn(self, headers=None):
    session = requests.Session()
    if self.http_conn_id:
        conn = self.get_connection(self.http_conn_id)
        if '://' in conn.host:
            self.base_url = conn.host
        else:
            schema = conn.schema if conn.schema else 'http'
            self.base_url = schema + '://' + conn.host
        if conn.port:
            self.base_url = self.base_url + ':' + str(conn.port)
        if conn.login:
            session.auth = (conn.login, conn.password)
        if conn.extra:
            try:
                session.headers.update(conn.extra_dejson)
            except TypeError:
                self.log.warn('Connection to %s has invalid extra field.', conn.host)
    if headers:
        session.headers.update(headers)
    return session