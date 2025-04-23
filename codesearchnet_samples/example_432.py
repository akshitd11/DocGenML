def make_query(self, query):
    conn = self.get_conn()
    self.log.info('Querying for all objects')
    query_results = conn.query_all(query)
    self.log.info('Received results: Total size: %s; Done: %s', query_results['totalSize'], query_results['done'])
    return query_results