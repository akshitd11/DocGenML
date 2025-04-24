def flush(self):
    if len(self._buffer) > 0:
        self.logger.log(self.level, self._buffer)
        self._buffer = str()