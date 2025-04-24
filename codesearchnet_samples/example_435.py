def get_object_from_salesforce(self, obj, fields):
    query = 'SELECT {} FROM {}'.format(','.join(fields), obj)
    self.log.info('Making query to Salesforce: %s', query if len(query) < 30 else ' ... '.join([query[:15], query[-15:]]))
    return self.make_query(query)