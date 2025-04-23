def insert_one(self, mongo_collection, doc, mongo_db=None, **kwargs):
    collection = self.get_collection(mongo_collection, mongo_db=mongo_db)
    return collection.insert_one(doc, **kwargs)