def retrieve_file(self, remote_full_path, local_full_path_or_buffer, callback=None):
    conn = self.get_conn()
    is_path = isinstance(local_full_path_or_buffer, basestring)
    if not callback:
        if is_path:
            output_handle = open(local_full_path_or_buffer, 'wb')
        else:
            output_handle = local_full_path_or_buffer
        callback = output_handle.write
    else:
        output_handle = None
    (remote_path, remote_file_name) = os.path.split(remote_full_path)
    conn.cwd(remote_path)
    self.log.info('Retrieving file from FTP: %s', remote_full_path)
    conn.retrbinary('RETR %s' % remote_file_name, callback)
    self.log.info('Finished retrieving file from FTP: %s', remote_full_path)
    if is_path and output_handle:
        output_handle.close()