def get_conn(self):
    self.log.debug('Creating SSH client for conn_id: %s', self.ssh_conn_id)
    client = paramiko.SSHClient()
    if not self.allow_host_key_change:
        self.log.warning('Remote Identification Change is not verified. This wont protect against Man-In-The-Middle attacks')
        client.load_system_host_keys()
    if self.no_host_key_check:
        self.log.warning('No Host Key Verification. This wont protect against Man-In-The-Middle attacks')
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    if self.password and self.password.strip():
        client.connect(hostname=self.remote_host, username=self.username, password=self.password, key_filename=self.key_file, timeout=self.timeout, compress=self.compress, port=self.port, sock=self.host_proxy)
    else:
        client.connect(hostname=self.remote_host, username=self.username, key_filename=self.key_file, timeout=self.timeout, compress=self.compress, port=self.port, sock=self.host_proxy)
    if self.keepalive_interval:
        client.get_transport().set_keepalive(self.keepalive_interval)
    self.client = client
    return client