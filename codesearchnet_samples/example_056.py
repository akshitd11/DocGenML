def get_uri(self):
    conn_config = self._get_conn_params()
    uri = 'snowflake://{user}:{password}@{account}/{database}/'
    uri += '{schema}?warehouse={warehouse}&role={role}'
    return uri.format(**conn_config)