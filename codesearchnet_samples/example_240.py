def get_conn(self):
    if not self._conn:
        self._conn = LanguageServiceClient(credentials=self._get_credentials())
    return self._conn