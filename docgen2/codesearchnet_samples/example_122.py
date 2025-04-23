def get_conn(self):
    conn = self.get_connection(self.druid_broker_conn_id)
    druid_broker_conn = connect(host=conn.host, port=conn.port, path=conn.extra_dejson.get('endpoint', '/druid/v2/sql'), scheme=conn.extra_dejson.get('schema', 'http'))
    self.log.info('Get the connection to druid broker on %s', conn.host)
    return druid_broker_conn