def get_conn(self):
    if not self.conn:
        connection = self.get_connection(self.conn_id)
        extras = connection.extra_dejson
        self.conn = Salesforce(username=connection.login, password=connection.password, security_token=extras['security_token'], instance_url=connection.host, sandbox=extras.get('sandbox', False))
    return self.conn