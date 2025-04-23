def start(self):
    self._process = self._launch_process(self._dag_directory, self._file_paths, self._max_runs, self._processor_factory, self._child_signal_conn, self._stat_queue, self._result_queue, self._async_mode)
    self.log.info('Launched DagFileProcessorManager with pid: %s', self._process.pid)