def wasb_log_exists(self, remote_log_location):
    try:
        return self.hook.check_for_blob(self.wasb_container, remote_log_location)
    except Exception:
        pass
    return False