def gcs_write(self, log, remote_log_location, append=True):
    if append:
        try:
            old_log = self.gcs_read(remote_log_location)
            log = '\n'.join([old_log, log]) if old_log else log
        except Exception as e:
            if not hasattr(e, 'resp') or e.resp.get('status') != '404':
                log = '*** Previous log discarded: {}\n\n'.format(str(e)) + log
    try:
        (bkt, blob) = self.parse_gcs_url(remote_log_location)
        from tempfile import NamedTemporaryFile
        with NamedTemporaryFile(mode='w+') as tmpfile:
            tmpfile.write(log)
            tmpfile.flush()
            self.hook.upload(bkt, blob, tmpfile.name)
    except Exception as e:
        self.log.error('Could not write logs to %s: %s', remote_log_location, e)