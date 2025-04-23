def create_connection(self, session=None):
    connection = Connection(conn_id=self.db_conn_id)
    uri = self._generate_connection_uri()
    self.log.info('Creating connection %s', self.db_conn_id)
    connection.parse_from_uri(uri)
    session.add(connection)
    session.commit()