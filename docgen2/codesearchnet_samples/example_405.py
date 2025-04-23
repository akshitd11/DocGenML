def _read(self, ti, try_number, metadata=None):
    log_relative_path = self._render_filename(ti, try_number)
    location = os.path.join(self.local_base, log_relative_path)
    log = ''
    if os.path.exists(location):
        try:
            with open(location) as f:
                log += '*** Reading local file: {}\n'.format(location)
                log += ''.join(f.readlines())
        except Exception as e:
            log = '*** Failed to load local log file: {}\n'.format(location)
            log += '*** {}\n'.format(str(e))
    else:
        url = os.path.join('http://{ti.hostname}:{worker_log_server_port}/log', log_relative_path).format(ti=ti, worker_log_server_port=conf.get('celery', 'WORKER_LOG_SERVER_PORT'))
        log += '*** Log file does not exist: {}\n'.format(location)
        log += '*** Fetching from: {}\n'.format(url)
        try:
            timeout = None
            try:
                timeout = conf.getint('webserver', 'log_fetch_timeout_sec')
            except (AirflowConfigException, ValueError):
                pass
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            log += '\n' + response.text
        except Exception as e:
            log += '*** Failed to fetch log file from worker. {}\n'.format(str(e))
    return (log, {'end_of_log': True})