def _read(self, ti, try_number, metadata=None):
    log_relative_path = self._render_filename(ti, try_number)
    remote_loc = os.path.join(self.remote_base, log_relative_path)
    if self.wasb_log_exists(remote_loc):
        remote_log = self.wasb_read(remote_loc, return_error=True)
        log = '*** Reading remote log from {}.\n{}\n'.format(remote_loc, remote_log)
        return (log, {'end_of_log': True})
    else:
        return super()._read(ti, try_number)