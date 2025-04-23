def delete_database(self, database_name):
    if database_name is None:
        raise AirflowBadRequest('Database name cannot be None.')
    self.get_conn().DeleteDatabase(get_database_link(database_name))