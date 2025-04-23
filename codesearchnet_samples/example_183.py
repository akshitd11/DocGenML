def end(self):
    if not self._process:
        self.log.warn('Ending without manager process.')
        return
    this_process = psutil.Process(os.getpid())
    try:
        manager_process = psutil.Process(self._process.pid)
    except psutil.NoSuchProcess:
        self.log.info('Manager process not running.')
        return
    if manager_process.is_running() and manager_process.pid in [x.pid for x in this_process.children()]:
        self.log.info('Terminating manager process: %s', manager_process.pid)
        manager_process.terminate()
        timeout = 5
        self.log.info('Waiting up to %ss for manager process to exit...', timeout)
        try:
            psutil.wait_procs({manager_process}, timeout)
        except psutil.TimeoutExpired:
            self.log.debug('Ran out of time while waiting for processes to exit')
    if manager_process.is_running() and manager_process.pid in [x.pid for x in this_process.children()]:
        self.log.info('Killing manager process: %s', manager_process.pid)
        manager_process.kill()
        manager_process.wait()