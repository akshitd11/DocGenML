def jenkins_request_with_headers(jenkins_server, req):
    try:
        response = jenkins_server.jenkins_request(req)
        response_body = response.content
        response_headers = response.headers
        if response_body is None:
            raise jenkins.EmptyResponseException('Error communicating with server[%s]: empty response' % jenkins_server.server)
        return {'body': response_body.decode('utf-8'), 'headers': response_headers}
    except HTTPError as e:
        if e.code in [401, 403, 500]:
            raise JenkinsException('Error in request. ' + 'Possibly authentication failed [%s]: %s' % (e.code, e.msg))
        elif e.code == 404:
            raise jenkins.NotFoundException('Requested item could not be found')
        else:
            raise
    except socket.timeout as e:
        raise jenkins.TimeoutException('Error in request: %s' % e)
    except URLError as e:
        if str(e.reason) == 'timed out':
            raise jenkins.TimeoutException('Error in request: %s' % e.reason)
        raise JenkinsException('Error in request: %s' % e.reason)