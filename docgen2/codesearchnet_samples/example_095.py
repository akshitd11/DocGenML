def retrieve_connection(self, session=None):
    self.log.info('Retrieving connection %s', self.db_conn_id)
    connections = session.query(Connection).filter(Connection.conn_id == self.db_conn_id)
    if connections.count():
        return connections[0]
    return None