def get_document(self, document_id, database_name=None, collection_name=None):
    if document_id is None:
        raise AirflowBadRequest('Cannot get a document without an id')
    try:
        return self.get_conn().ReadItem(get_document_link(self.__get_database_name(database_name), self.__get_collection_name(collection_name), document_id))
    except HTTPFailure:
        return None