def run(self, endpoint, data=None, headers=None, extra_options=None):
    extra_options = extra_options or {}
    session = self.get_conn(headers)
    if self.base_url and (not self.base_url.endswith('/')) and endpoint and (not endpoint.startswith('/')):
        url = self.base_url + '/' + endpoint
    else:
        url = (self.base_url or '') + (endpoint or '')
    req = None
    if self.method == 'GET':
        req = requests.Request(self.method, url, params=data, headers=headers)
    elif self.method == 'HEAD':
        req = requests.Request(self.method, url, headers=headers)
    else:
        req = requests.Request(self.method, url, data=data, headers=headers)
    prepped_request = session.prepare_request(req)
    self.log.info("Sending '%s' to url: %s", self.method, url)
    return self.run_and_check(session, prepped_request, extra_options)