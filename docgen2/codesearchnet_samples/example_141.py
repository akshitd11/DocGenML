def does_database_exist(self, database_name):
    if database_name is None:
        raise AirflowBadRequest('Database name cannot be None.')
    existing_database = list(self.get_conn().QueryDatabases({'query': 'SELECT * FROM r WHERE r.id=@id', 'parameters': [{'name': '@id', 'value': database_name}]}))
    if len(existing_database) == 0:
        return False
    return True