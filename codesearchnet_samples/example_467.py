def get_file(self, file_path, container_name, blob_name, **kwargs):
    return self.connection.get_blob_to_path(container_name, blob_name, file_path, **kwargs)