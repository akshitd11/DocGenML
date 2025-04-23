def _sync_metadata(self):
    while not self._stat_queue.empty():
        stat = self._stat_queue.get()
        self._file_paths = stat.file_paths
        self._all_pids = stat.all_pids
        self._done = stat.done
        self._all_files_processed = stat.all_files_processed
        self._result_count += stat.result_count