def _heartbeat_manager(self):
    if self._process and (not self._process.is_alive()) and (not self.done):
        self.start()