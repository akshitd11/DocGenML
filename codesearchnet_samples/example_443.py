def get_collection(self, mongo_collection, mongo_db=None):
    mongo_db = mongo_db if mongo_db is not None else self.connection.schema
    mongo_conn = self.get_conn()
    return mongo_conn.get_database(mongo_db).get_collection(mongo_collection)