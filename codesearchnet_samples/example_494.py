def get_file_to_stream(self, stream, share_name, directory_name, file_name, **kwargs):
    self.connection.get_file_to_stream(share_name, directory_name, file_name, stream, **kwargs)