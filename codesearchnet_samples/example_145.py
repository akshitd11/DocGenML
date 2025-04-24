def upsert_document(self, document, database_name=None, collection_name=None, document_id=None):
    if document_id is None:
        document_id = str(uuid.uuid4())
    if document is None:
        raise AirflowBadRequest('You cannot insert a None document')
    if 'id' in document:
        if document['id'] is None:
            document['id'] = document_id
    else:
        document['id'] = document_id
    created_document = self.get_conn().CreateItem(get_collection_link(self.__get_database_name(database_name), self.__get_collection_name(collection_name)), document)
    return created_document