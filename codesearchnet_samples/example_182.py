def terminate(self):
    self.log.info('Sending termination message to manager.')
    self._child_signal_conn.send(DagParsingSignal.TERMINATE_MANAGER)