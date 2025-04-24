def delete_document(self, document_id, database_name=None, collection_name=None):
    if document_id is None:
        raise AirflowBadRequest('Cannot delete a document without an id')
    self.get_conn().DeleteItem(get_document_link(self.__get_database_name(database_name), self.__get_collection_name(collection_name), document_id))