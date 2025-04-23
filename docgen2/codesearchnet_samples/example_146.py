def insert_documents(self, documents, database_name=None, collection_name=None):
    if documents is None:
        raise AirflowBadRequest('You cannot insert empty documents')
    created_documents = []
    for single_document in documents:
        created_documents.append(self.get_conn().CreateItem(get_collection_link(self.__get_database_name(database_name), self.__get_collection_name(collection_name)), single_document))
    return created_documents