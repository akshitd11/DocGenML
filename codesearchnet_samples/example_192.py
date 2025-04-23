def get_pid(self, file_path):
    if file_path in self._processors:
        return self._processors[file_path].pid
    return None