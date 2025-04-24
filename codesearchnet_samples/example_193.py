def get_runtime(self, file_path):
    if file_path in self._processors:
        return (timezone.utcnow() - self._processors[file_path].start_time).total_seconds()
    return None