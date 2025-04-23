def list_directories_and_files(self, share_name, directory_name=None, **kwargs):
    return self.connection.list_directories_and_files(share_name, directory_name, **kwargs)