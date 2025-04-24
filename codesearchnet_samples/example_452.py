def delete_many(self, mongo_collection, filter_doc, mongo_db=None, **kwargs):
    collection = self.get_collection(mongo_collection, mongo_db=mongo_db)
    return collection.delete_many(filter_doc, **kwargs)