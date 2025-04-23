def get_start_time(self, file_path):
    if file_path in self._processors:
        return self._processors[file_path].start_time
    return None