def write(self, message):
    if not message.endswith('\n'):
        self._buffer += message
    else:
        self._buffer += message
        self.logger.log(self.level, self._buffer.rstrip())
        self._buffer = str()