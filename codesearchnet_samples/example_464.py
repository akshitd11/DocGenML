def check_for_prefix(self, container_name, prefix, **kwargs):
    matches = self.connection.list_blobs(container_name, prefix, num_results=1, **kwargs)
    return len(list(matches)) > 0