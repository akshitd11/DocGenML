def delete_collection(self, collection_name, database_name=None):
    if collection_name is None:
        raise AirflowBadRequest('Collection name cannot be None.')
    self.get_conn().DeleteContainer(get_collection_link(self.__get_database_name(database_name), collection_name))