def heartbeat(self):
    finished_processors = {}
    ':type : dict[unicode, AbstractDagFileProcessor]'
    running_processors = {}
    ':type : dict[unicode, AbstractDagFileProcessor]'
    for (file_path, processor) in self._processors.items():
        if processor.done:
            self.log.debug('Processor for %s finished', file_path)
            now = timezone.utcnow()
            finished_processors[file_path] = processor
            self._last_runtime[file_path] = (now - processor.start_time).total_seconds()
            self._last_finish_time[file_path] = now
            self._run_count[file_path] += 1
        else:
            running_processors[file_path] = processor
    self._processors = running_processors
    self.log.debug('%s/%s DAG parsing processes running', len(self._processors), self._parallelism)
    self.log.debug('%s file paths queued for processing', len(self._file_path_queue))
    simple_dags = []
    for (file_path, processor) in finished_processors.items():
        if processor.result is None:
            self.log.warning('Processor for %s exited with return code %s.', processor.file_path, processor.exit_code)
        else:
            for simple_dag in processor.result:
                simple_dags.append(simple_dag)
    if len(self._file_path_queue) == 0:
        file_paths_in_progress = self._processors.keys()
        now = timezone.utcnow()
        file_paths_recently_processed = []
        for file_path in self._file_paths:
            last_finish_time = self.get_last_finish_time(file_path)
            if last_finish_time is not None and (now - last_finish_time).total_seconds() < self._file_process_interval:
                file_paths_recently_processed.append(file_path)
        files_paths_at_run_limit = [file_path for (file_path, num_runs) in self._run_count.items() if num_runs == self._max_runs]
        files_paths_to_queue = list(set(self._file_paths) - set(file_paths_in_progress) - set(file_paths_recently_processed) - set(files_paths_at_run_limit))
        for (file_path, processor) in self._processors.items():
            self.log.debug('File path %s is still being processed (started: %s)', processor.file_path, processor.start_time.isoformat())
        self.log.debug('Queuing the following files for processing:\n\t%s', '\n\t'.join(files_paths_to_queue))
        self._file_path_queue.extend(files_paths_to_queue)
    zombies = self._find_zombies()
    while self._parallelism - len(self._processors) > 0 and len(self._file_path_queue) > 0:
        file_path = self._file_path_queue.pop(0)
        processor = self._processor_factory(file_path, zombies)
        processor.start()
        self.log.debug('Started a process (PID: %s) to generate tasks for %s', processor.pid, file_path)
        self._processors[file_path] = processor
    self._run_count[self._heart_beat_key] += 1
    return simple_dags