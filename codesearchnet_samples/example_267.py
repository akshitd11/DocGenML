def _num_tasks_per_fetch_process(self):
    return max(1, int(math.ceil(1.0 * len(self.tasks) / self._sync_parallelism)))