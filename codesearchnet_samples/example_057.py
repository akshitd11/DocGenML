def get_conn(self):
    conn_config = self._get_conn_params()
    conn = snowflake.connector.connect(**conn_config)
    return conn