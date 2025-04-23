def execute_work(self, key, command):
    if key is None:
        return
    self.log.info('%s running %s', self.__class__.__name__, command)
    try:
        subprocess.check_call(command, close_fds=True)
        state = State.SUCCESS
    except subprocess.CalledProcessError as e:
        state = State.FAILED
        self.log.error('Failed to execute task %s.', str(e))
    self.result_queue.put((key, state))