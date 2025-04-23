def get_proxy_version(self):
    self._download_sql_proxy_if_needed()
    command_to_run = [self.sql_proxy_path]
    command_to_run.extend(['--version'])
    command_to_run.extend(self._get_credential_parameters())
    result = subprocess.check_output(command_to_run).decode('utf-8')
    pattern = re.compile('^.*[V|v]ersion ([^;]*);.*$')
    m = pattern.match(result)
    if m:
        return m.group(1)
    else:
        return None