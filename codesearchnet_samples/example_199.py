def max_runs_reached(self):
    if self._max_runs == -1:
        return False
    for file_path in self._file_paths:
        if self._run_count[file_path] < self._max_runs:
            return False
    if self._run_count[self._heart_beat_key] < self._max_runs:
        return False
    return True