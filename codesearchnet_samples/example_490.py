def check_for_file(self, share_name, directory_name, file_name, **kwargs):
    return self.connection.exists(share_name, directory_name, file_name, **kwargs)