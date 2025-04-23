def replace_many(self, mongo_collection, docs, filter_docs=None, mongo_db=None, upsert=False, collation=None, **kwargs):
    collection = self.get_collection(mongo_collection, mongo_db=mongo_db)
    if not filter_docs:
        filter_docs = [{'_id': doc['_id']} for doc in docs]
    requests = [ReplaceOne(filter_docs[i], docs[i], upsert=upsert, collation=collation) for i in range(len(docs))]
    return collection.bulk_write(requests, **kwargs)