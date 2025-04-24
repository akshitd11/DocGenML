def get_conn(self):
    db = self.get_connection(self.presto_conn_id)
    reqkwargs = None
    if db.password is not None:
        reqkwargs = {'auth': HTTPBasicAuth(db.login, db.password)}
    return presto.connect(host=db.host, port=db.port, username=db.login, source=db.extra_dejson.get('source', 'airflow'), protocol=db.extra_dejson.get('protocol', 'http'), catalog=db.extra_dejson.get('catalog', 'hive'), requests_kwargs=reqkwargs, schema=db.schema)