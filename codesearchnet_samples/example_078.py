def get_conn(self):
    if not self._client:
        self._client = Client(credentials=self._get_credentials())
    return self._client