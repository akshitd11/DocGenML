def _log_file_processing_stats(self, known_file_paths):
    headers = ['File Path', 'PID', 'Runtime', 'Last Runtime', 'Last Run']
    rows = []
    for file_path in known_file_paths:
        last_runtime = self.get_last_runtime(file_path)
        file_name = os.path.basename(file_path)
        file_name = os.path.splitext(file_name)[0].replace(os.sep, '.')
        if last_runtime:
            Stats.gauge('dag_processing.last_runtime.{}'.format(file_name), last_runtime)
        processor_pid = self.get_pid(file_path)
        processor_start_time = self.get_start_time(file_path)
        runtime = (timezone.utcnow() - processor_start_time).total_seconds() if processor_start_time else None
        last_run = self.get_last_finish_time(file_path)
        if last_run:
            seconds_ago = (timezone.utcnow() - last_run).total_seconds()
            Stats.gauge('dag_processing.last_run.seconds_ago.{}'.format(file_name), seconds_ago)
        rows.append((file_path, processor_pid, runtime, last_runtime, last_run))
    rows = sorted(rows, key=lambda x: x[3] or 0.0)
    formatted_rows = []
    for (file_path, pid, runtime, last_runtime, last_run) in rows:
        formatted_rows.append((file_path, pid, '{:.2f}s'.format(runtime) if runtime else None, '{:.2f}s'.format(last_runtime) if last_runtime else None, last_run.strftime('%Y-%m-%dT%H:%M:%S') if last_run else None))
    log_str = '\n' + '=' * 80 + '\n' + 'DAG File Processing Stats\n\n' + tabulate(formatted_rows, headers=headers) + '\n' + '=' * 80
    self.log.info(log_str)