def set_file_paths(self, new_file_paths):
    self._file_paths = new_file_paths
    self._file_path_queue = [x for x in self._file_path_queue if x in new_file_paths]
    filtered_processors = {}
    for (file_path, processor) in self._processors.items():
        if file_path in new_file_paths:
            filtered_processors[file_path] = processor
        else:
            self.log.warning('Stopping processor for %s', file_path)
            processor.terminate()
    self._processors = filtered_processors