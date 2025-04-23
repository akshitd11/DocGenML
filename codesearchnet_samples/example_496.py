def load_string(self, string_data, share_name, directory_name, file_name, **kwargs):
    self.connection.create_file_from_text(share_name, directory_name, file_name, string_data, **kwargs)