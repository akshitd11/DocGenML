def start_proxy(self):
    self._download_sql_proxy_if_needed()
    if self.sql_proxy_process:
        raise AirflowException('The sql proxy is already running: {}'.format(self.sql_proxy_process))
    else:
        command_to_run = [self.sql_proxy_path]
        command_to_run.extend(self.command_line_parameters)
        try:
            self.log.info('Creating directory %s', self.cloud_sql_proxy_socket_directory)
            os.makedirs(self.cloud_sql_proxy_socket_directory)
        except OSError:
            pass
        command_to_run.extend(self._get_credential_parameters())
        self.log.info('Running the command: `%s`', ' '.join(command_to_run))
        self.sql_proxy_process = Popen(command_to_run, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        self.log.info('The pid of cloud_sql_proxy: %s', self.sql_proxy_process.pid)
        while True:
            line = self.sql_proxy_process.stderr.readline().decode('utf-8')
            return_code = self.sql_proxy_process.poll()
            if line == '' and return_code is not None:
                self.sql_proxy_process = None
                raise AirflowException('The cloud_sql_proxy finished early with return code {}!'.format(return_code))
            if line != '':
                self.log.info(line)
            if 'googleapi: Error' in line or 'invalid instance name:' in line:
                self.stop_proxy()
                raise AirflowException('Error when starting the cloud_sql_proxy {}!'.format(line))
            if 'Ready for new connections' in line:
                return