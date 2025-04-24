def wasb_write(self, log, remote_log_location, append=True):
    if append and self.wasb_log_exists(remote_log_location):
        old_log = self.wasb_read(remote_log_location)
        log = '\n'.join([old_log, log]) if old_log else log
    try:
        self.hook.load_string(log, self.wasb_container, remote_log_location)
    except AzureHttpError:
        self.log.exception('Could not write logs to %s', remote_log_location)