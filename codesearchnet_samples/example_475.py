def store_file(self, remote_full_path, local_full_path_or_buffer):
    conn = self.get_conn()
    is_path = isinstance(local_full_path_or_buffer, basestring)
    if is_path:
        input_handle = open(local_full_path_or_buffer, 'rb')
    else:
        input_handle = local_full_path_or_buffer
    (remote_path, remote_file_name) = os.path.split(remote_full_path)
    conn.cwd(remote_path)
    conn.storbinary('STOR %s' % remote_file_name, input_handle)
    if is_path:
        input_handle.close()