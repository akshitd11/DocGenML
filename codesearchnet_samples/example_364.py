def close(self):
    if self.closed:
        return
    super().close()
    if not self.upload_on_close:
        return
    local_loc = os.path.join(self.local_base, self.log_relative_path)
    remote_loc = os.path.join(self.remote_base, self.log_relative_path)
    if os.path.exists(local_loc):
        with open(local_loc, 'r') as logfile:
            log = logfile.read()
        self.wasb_write(log, remote_loc, append=True)
        if self.delete_local_copy:
            shutil.rmtree(os.path.dirname(local_loc))
    self.closed = True