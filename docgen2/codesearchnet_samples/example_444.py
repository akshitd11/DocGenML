def aggregate(self, mongo_collection, aggregate_query, mongo_db=None, **kwargs):
    collection = self.get_collection(mongo_collection, mongo_db=mongo_db)
    return collection.aggregate(aggregate_query, **kwargs)