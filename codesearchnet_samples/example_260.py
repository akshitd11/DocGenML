def get_conn(self):
    http_authorized = self._authorize()
    return build('dataproc', self.api_version, http=http_authorized, cache_discovery=False)