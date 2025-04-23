def get_sqlproxy_runner(self):
    if not self.use_proxy:
        raise AirflowException('Proxy runner can only be retrieved in case of use_proxy = True')
    return CloudSqlProxyRunner(path_prefix=self.sql_proxy_unique_path, instance_specification=self._get_sqlproxy_instance_specification(), project_id=self.project_id, sql_proxy_version=self.sql_proxy_version, sql_proxy_binary_path=self.sql_proxy_binary_path)