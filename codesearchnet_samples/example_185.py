def start(self):
    self.log.info('Processing files using up to %s processes at a time ', self._parallelism)
    self.log.info('Process each file at most once every %s seconds', self._file_process_interval)
    self.log.info('Checking for new files in %s every %s seconds', self._dag_directory, self.dag_dir_list_interval)
    if self._async_mode:
        self.log.debug('Starting DagFileProcessorManager in async mode')
        self.start_in_async()
    else:
        self.log.debug('Starting DagFileProcessorManager in sync mode')
        self.start_in_sync()