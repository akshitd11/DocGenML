def get_documents(self, sql_string, database_name=None, collection_name=None, partition_key=None):
    if sql_string is None:
        raise AirflowBadRequest('SQL query string cannot be None')
    query = {'query': sql_string}
    try:
        result_iterable = self.get_conn().QueryItems(get_collection_link(self.__get_database_name(database_name), self.__get_collection_name(collection_name)), query, partition_key)
        return list(result_iterable)
    except HTTPFailure:
        return None