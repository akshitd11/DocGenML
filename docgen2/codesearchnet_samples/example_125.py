def check_response(self, response):
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        self.log.error('HTTP error: %s', response.reason)
        if self.method not in ['GET', 'HEAD']:
            self.log.error(response.text)
        raise AirflowException(str(response.status_code) + ':' + response.reason)