def try_number(self):
    if self.state == State.RUNNING:
        return self._try_number
    return self._try_number + 1