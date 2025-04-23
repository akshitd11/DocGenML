def get_conn(self):
    if self.client is not None:
        return self.client
    options = self.extras
    if options.get('ssl', False):
        options.update({'ssl_cert_reqs': CERT_NONE})
    self.client = MongoClient(self.uri, **options)
    return self.client