def check_for_directory(self, share_name, directory_name, **kwargs):
    return self.connection.exists(share_name, directory_name, **kwargs)