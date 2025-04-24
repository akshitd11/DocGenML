def get_conn(self):
    if not self._conn:
        http_authorized = self._authorize()
        self._conn = build('compute', self.api_version, http=http_authorized, cache_discovery=False)
    return self._conn