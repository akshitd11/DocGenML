def load_file(self, file_path, container_name, blob_name, **kwargs):
    self.connection.create_blob_from_path(container_name, blob_name, file_path, **kwargs)