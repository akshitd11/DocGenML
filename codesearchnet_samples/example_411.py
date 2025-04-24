def get_conn(self):
    conn = self.get_connection(self.conn_id)
    service_options = conn.extra_dejson
    self.account_name = service_options.get('account_name')
    adlCreds = lib.auth(tenant_id=service_options.get('tenant'), client_secret=conn.password, client_id=conn.login)
    adlsFileSystemClient = core.AzureDLFileSystem(adlCreds, store_name=self.account_name)
    adlsFileSystemClient.connect()
    return adlsFileSystemClient