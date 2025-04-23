def insert_many(self, mongo_collection, docs, mongo_db=None, **kwargs):
    collection = self.get_collection(mongo_collection, mongo_db=mongo_db)
    return collection.insert_many(docs, **kwargs)