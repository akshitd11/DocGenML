def poll_operation_until_done(self, name, polling_interval_in_seconds):
    while True:
        result = self.get_operation(name)
        state = result['metadata']['common']['state']
        if state == 'PROCESSING':
            self.log.info('Operation is processing. Re-polling state in {} seconds'.format(polling_interval_in_seconds))
            time.sleep(polling_interval_in_seconds)
        else:
            return result