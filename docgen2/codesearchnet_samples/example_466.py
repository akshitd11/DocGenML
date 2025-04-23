def load_string(self, string_data, container_name, blob_name, **kwargs):
    self.connection.create_blob_from_text(container_name, blob_name, string_data, **kwargs)