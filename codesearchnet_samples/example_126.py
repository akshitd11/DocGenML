def run_and_check(self, session, prepped_request, extra_options):
    extra_options = extra_options or {}
    try:
        response = session.send(prepped_request, stream=extra_options.get('stream', False), verify=extra_options.get('verify', True), proxies=extra_options.get('proxies', {}), cert=extra_options.get('cert'), timeout=extra_options.get('timeout'), allow_redirects=extra_options.get('allow_redirects', True))
        if extra_options.get('check_response', True):
            self.check_response(response)
        return response
    except requests.exceptions.ConnectionError as ex:
        self.log.warn(str(ex) + ' Tenacity will retry to execute the operation')
        raise ex