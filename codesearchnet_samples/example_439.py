def gcs_read(self, remote_log_location):
    (bkt, blob) = self.parse_gcs_url(remote_log_location)
    return self.hook.download(bkt, blob).decode('utf-8')