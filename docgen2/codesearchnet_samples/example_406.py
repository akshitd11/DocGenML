def read(self, task_instance, try_number=None, metadata=None):
    if try_number is None:
        next_try = task_instance.next_try_number
        try_numbers = list(range(1, next_try))
    elif try_number < 1:
        logs = ['Error fetching the logs. Try number {} is invalid.'.format(try_number)]
        return logs
    else:
        try_numbers = [try_number]
    logs = [''] * len(try_numbers)
    metadatas = [{}] * len(try_numbers)
    for (i, try_number) in enumerate(try_numbers):
        (log, metadata) = self._read(task_instance, try_number, metadata)
        logs[i] += log
        metadatas[i] = metadata
    return (logs, metadatas)