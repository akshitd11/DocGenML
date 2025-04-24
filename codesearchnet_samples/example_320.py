def poll_job_in_queue(self, location, jenkins_server):
    try_count = 0
    location = location + '/api/json'
    self.log.info('Polling jenkins queue at the url %s', location)
    while try_count < self.max_try_before_job_appears:
        location_answer = jenkins_request_with_headers(jenkins_server, Request(location))
        if location_answer is not None:
            json_response = json.loads(location_answer['body'])
            if 'executable' in json_response:
                build_number = json_response['executable']['number']
                self.log.info('Job executed on Jenkins side with the build number %s', build_number)
                return build_number
        try_count += 1
        time.sleep(self.sleep_time)
    raise AirflowException("The job hasn't been executed after polling the queue %d times", self.max_try_before_job_appears)