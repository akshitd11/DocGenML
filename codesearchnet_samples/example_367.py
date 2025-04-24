def wasb_read(self, remote_log_location, return_error=False):
    try:
        return self.hook.read_file(self.wasb_container, remote_log_location)
    except AzureHttpError:
        msg = 'Could not read logs from {}'.format(remote_log_location)
        self.log.exception(msg)
        if return_error:
            return msg