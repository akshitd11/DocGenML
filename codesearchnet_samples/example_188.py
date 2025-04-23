def _refresh_dag_dir(self):
    elapsed_time_since_refresh = (timezone.utcnow() - self.last_dag_dir_refresh_time).total_seconds()
    if elapsed_time_since_refresh > self.dag_dir_list_interval:
        self.log.info('Searching for files in %s', self._dag_directory)
        self._file_paths = list_py_file_paths(self._dag_directory)
        self.last_dag_dir_refresh_time = timezone.utcnow()
        self.log.info('There are %s files in %s', len(self._file_paths), self._dag_directory)
        self.set_file_paths(self._file_paths)
        try:
            self.log.debug('Removing old import errors')
            self.clear_nonexistent_import_errors()
        except Exception:
            self.log.exception('Error removing old import errors')