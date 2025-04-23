def next_retry_datetime(self):
    delay = self.task.retry_delay
    if self.task.retry_exponential_backoff:
        min_backoff = int(delay.total_seconds() * 2 ** (self.try_number - 2))
        hash = int(hashlib.sha1('{}#{}#{}#{}'.format(self.dag_id, self.task_id, self.execution_date, self.try_number).encode('utf-8')).hexdigest(), 16)
        modded_hash = min_backoff + hash % min_backoff
        delay_backoff_in_seconds = min(modded_hash, timedelta.max.total_seconds() - 1)
        delay = timedelta(seconds=delay_backoff_in_seconds)
        if self.task.max_retry_delay:
            delay = min(self.task.max_retry_delay, delay)
    return self.end_date + delay