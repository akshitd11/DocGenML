def _do_api_call(self, endpoint_info, json):
    (method, endpoint) = endpoint_info
    url = 'https://{host}/{endpoint}'.format(host=self._parse_host(self.databricks_conn.host), endpoint=endpoint)
    if 'token' in self.databricks_conn.extra_dejson:
        self.log.info('Using token auth.')
        auth = _TokenAuth(self.databricks_conn.extra_dejson['token'])
    else:
        self.log.info('Using basic auth.')
        auth = (self.databricks_conn.login, self.databricks_conn.password)
    if method == 'GET':
        request_func = requests.get
    elif method == 'POST':
        request_func = requests.post
    else:
        raise AirflowException('Unexpected HTTP Method: ' + method)
    attempt_num = 1
    while True:
        try:
            response = request_func(url, json=json, auth=auth, headers=USER_AGENT_HEADER, timeout=self.timeout_seconds)
            response.raise_for_status()
            return response.json()
        except requests_exceptions.RequestException as e:
            if not _retryable_error(e):
                raise AirflowException('Response: {0}, Status Code: {1}'.format(e.response.content, e.response.status_code))
            self._log_request_error(attempt_num, e)
        if attempt_num == self.retry_limit:
            raise AirflowException(('API requests to Databricks failed {} times. ' + 'Giving up.').format(self.retry_limit))
        attempt_num += 1
        sleep(self.retry_delay)