def update_one(self, mongo_collection, filter_doc, update_doc, mongo_db=None, **kwargs):
    collection = self.get_collection(mongo_collection, mongo_db=mongo_db)
    return collection.update_one(filter_doc, update_doc, **kwargs)