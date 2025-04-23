def stop_proxy(self):
    if not self.sql_proxy_process:
        raise AirflowException('The sql proxy is not started yet')
    else:
        self.log.info('Stopping the cloud_sql_proxy pid: %s', self.sql_proxy_process.pid)
        self.sql_proxy_process.kill()
        self.sql_proxy_process = None
    self.log.info('Removing the socket directory: %s', self.cloud_sql_proxy_socket_directory)
    shutil.rmtree(self.cloud_sql_proxy_socket_directory, ignore_errors=True)
    if self.sql_proxy_was_downloaded:
        self.log.info('Removing downloaded proxy: %s', self.sql_proxy_path)
        try:
            os.remove(self.sql_proxy_path)
        except OSError as e:
            if not e.errno == errno.ENOENT:
                raise
    else:
        self.log.info('Skipped removing proxy - it was not downloaded: %s', self.sql_proxy_path)
    if os.path.isfile(self.credentials_path):
        self.log.info('Removing generated credentials file %s', self.credentials_path)
        os.remove(self.credentials_path)