def replace_one(self, mongo_collection, doc, filter_doc=None, mongo_db=None, **kwargs):
    collection = self.get_collection(mongo_collection, mongo_db=mongo_db)
    if not filter_doc:
        filter_doc = {'_id': doc['_id']}
    return collection.replace_one(filter_doc, doc, **kwargs)