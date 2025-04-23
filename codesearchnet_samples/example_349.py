def error(self, session=None):
    self.log.error('Recording the task instance as FAILED')
    self.state = State.FAILED
    session.merge(self)
    session.commit()