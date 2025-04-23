def find(self, mongo_collection, query, find_one=False, mongo_db=None, **kwargs):
    collection = self.get_collection(mongo_collection, mongo_db=mongo_db)
    if find_one:
        return collection.find_one(query, **kwargs)
    else:
        return collection.find(query, **kwargs)