def get_tunnel(self, remote_port, remote_host='localhost', local_port=None):
    if local_port:
        local_bind_address = ('localhost', local_port)
    else:
        local_bind_address = ('localhost',)
    if self.password and self.password.strip():
        client = SSHTunnelForwarder(self.remote_host, ssh_port=self.port, ssh_username=self.username, ssh_password=self.password, ssh_pkey=self.key_file, ssh_proxy=self.host_proxy, local_bind_address=local_bind_address, remote_bind_address=(remote_host, remote_port), logger=self.log)
    else:
        client = SSHTunnelForwarder(self.remote_host, ssh_port=self.port, ssh_username=self.username, ssh_pkey=self.key_file, ssh_proxy=self.host_proxy, local_bind_address=local_bind_address, remote_bind_address=(remote_host, remote_port), host_pkey_directories=[], logger=self.log)
    return client