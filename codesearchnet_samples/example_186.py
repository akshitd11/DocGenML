def start_in_async(self):
    while True:
        loop_start_time = time.time()
        if self._signal_conn.poll():
            agent_signal = self._signal_conn.recv()
            if agent_signal == DagParsingSignal.TERMINATE_MANAGER:
                self.terminate()
                break
            elif agent_signal == DagParsingSignal.END_MANAGER:
                self.end()
                sys.exit(os.EX_OK)
        self._refresh_dag_dir()
        simple_dags = self.heartbeat()
        for simple_dag in simple_dags:
            self._result_queue.put(simple_dag)
        self._print_stat()
        all_files_processed = all((self.get_last_finish_time(x) is not None for x in self.file_paths))
        max_runs_reached = self.max_runs_reached()
        dag_parsing_stat = DagParsingStat(self._file_paths, self.get_all_pids(), max_runs_reached, all_files_processed, len(simple_dags))
        self._stat_queue.put(dag_parsing_stat)
        if max_runs_reached:
            self.log.info('Exiting dag parsing loop as all files have been processed %s times', self._max_runs)
            break
        loop_duration = time.time() - loop_start_time
        if loop_duration < 1:
            sleep_length = 1 - loop_duration
            self.log.debug('Sleeping for %.2f seconds to prevent excessive logging', sleep_length)
            time.sleep(sleep_length)