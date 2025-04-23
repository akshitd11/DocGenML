def get_file(self, file_path, share_name, directory_name, file_name, **kwargs):
    self.connection.get_file_to_path(share_name, directory_name, file_name, file_path, **kwargs)