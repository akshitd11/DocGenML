def _query_cassandra(self):
    self.hook = CassandraHook(cassandra_conn_id=self.cassandra_conn_id)
    session = self.hook.get_conn()
    cursor = session.execute(self.cql)
    return cursor