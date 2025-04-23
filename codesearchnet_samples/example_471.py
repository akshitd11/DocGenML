def get_conn(self):
    if self.conn is None:
        params = self.get_connection(self.ftp_conn_id)
        pasv = params.extra_dejson.get('passive', True)
        self.conn = ftplib.FTP(params.host, params.login, params.password)
        self.conn.set_pasv(pasv)
    return self.conn