def create_collection(self, collection_name, database_name=None):
    if collection_name is None:
        raise AirflowBadRequest('Collection name cannot be None.')
    existing_container = list(self.get_conn().QueryContainers(get_database_link(self.__get_database_name(database_name)), {'query': 'SELECT * FROM r WHERE r.id=@id', 'parameters': [{'name': '@id', 'value': collection_name}]}))
    if len(existing_container) == 0:
        self.get_conn().CreateContainer(get_database_link(self.__get_database_name(database_name)), {'id': collection_name})