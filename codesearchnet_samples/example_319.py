def build_job(self, jenkins_server):
    if self.parameters and isinstance(self.parameters, six.string_types):
        import ast
        self.parameters = ast.literal_eval(self.parameters)
    if not self.parameters:
        self.parameters = None
    request = Request(jenkins_server.build_job_url(self.job_name, self.parameters, None))
    return jenkins_request_with_headers(jenkins_server, request)