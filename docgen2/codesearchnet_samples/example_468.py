def read_file(self, container_name, blob_name, **kwargs):
    return self.connection.get_blob_to_text(container_name, blob_name, **kwargs).content