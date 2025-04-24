def delete_connection(self, session=None):
    self.log.info('Deleting connection %s', self.db_conn_id)
    connections = session.query(Connection).filter(Connection.conn_id == self.db_conn_id)
    if connections.count():
        connection = connections[0]
        session.delete(connection)
        session.commit()
    else:
        self.log.info('Connection was already deleted!')