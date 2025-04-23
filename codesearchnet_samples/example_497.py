def load_stream(self, stream, share_name, directory_name, file_name, count, **kwargs):
    self.connection.create_file_from_stream(share_name, directory_name, file_name, stream, count, **kwargs)