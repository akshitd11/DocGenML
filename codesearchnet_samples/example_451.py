def delete_one(self, mongo_collection, filter_doc, mongo_db=None, **kwargs):
    collection = self.get_collection(mongo_collection, mongo_db=mongo_db)
    return collection.delete_one(filter_doc, **kwargs)