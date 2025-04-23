def harvest_simple_dags(self):
    self._sync_metadata()
    self._heartbeat_manager()
    simple_dags = []
    if sys.platform == 'darwin':
        qsize = self._result_count
    else:
        qsize = self._result_queue.qsize()
    for _ in range(qsize):
        simple_dags.append(self._result_queue.get())
    self._result_count = 0
    return simple_dags