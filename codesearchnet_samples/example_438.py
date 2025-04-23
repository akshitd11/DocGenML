def _read(self, ti, try_number, metadata=None):
    log_relative_path = self._render_filename(ti, try_number)
    remote_loc = os.path.join(self.remote_base, log_relative_path)
    try:
        remote_log = self.gcs_read(remote_loc)
        log = '*** Reading remote log from {}.\n{}\n'.format(remote_loc, remote_log)
        return (log, {'end_of_log': True})
    except Exception as e:
        log = '*** Unable to read remote log from {}\n*** {}\n\n'.format(remote_loc, str(e))
        self.log.error(log)
        (local_log, metadata) = super()._read(ti, try_number)
        log += local_log
        return (log, metadata)