def end(self):
    pids_to_kill = self.get_all_pids()
    if len(pids_to_kill) > 0:
        this_process = psutil.Process(os.getpid())
        child_processes = [x for x in this_process.children(recursive=True) if x.is_running() and x.pid in pids_to_kill]
        for child in child_processes:
            self.log.info('Terminating child PID: %s', child.pid)
            child.terminate()
        timeout = 5
        self.log.info('Waiting up to %s seconds for processes to exit...', timeout)
        try:
            psutil.wait_procs(child_processes, timeout=timeout, callback=lambda x: self.log.info('Terminated PID %s', x.pid))
        except psutil.TimeoutExpired:
            self.log.debug('Ran out of time while waiting for processes to exit')
        child_processes = [x for x in this_process.children(recursive=True) if x.is_running() and x.pid in pids_to_kill]
        if len(child_processes) > 0:
            self.log.info('SIGKILL processes that did not terminate gracefully')
            for child in child_processes:
                self.log.info('Killing child PID: %s', child.pid)
                child.kill()
                child.wait()