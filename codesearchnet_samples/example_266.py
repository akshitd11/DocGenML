def _num_tasks_per_send_process(self, to_send_count):
    return max(1, int(math.ceil(1.0 * to_send_count / self._sync_parallelism)))