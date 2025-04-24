def _print_stat(self):
    if (timezone.utcnow() - self.last_stat_print_time).total_seconds() > self.print_stats_interval:
        if len(self._file_paths) > 0:
            self._log_file_processing_stats(self._file_paths)
        self.last_stat_print_time = timezone.utcnow()