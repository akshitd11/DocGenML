def load_file(self, file_path, share_name, directory_name, file_name, **kwargs):
    self.connection.create_file_from_path(share_name, directory_name, file_name, file_path, **kwargs)