def check_for_blob(self, container_name, blob_name, **kwargs):
    return self.connection.exists(container_name, blob_name, **kwargs)