def delete_file(self, container_name, blob_name, is_prefix=False, ignore_if_missing=False, **kwargs):
    if is_prefix:
        blobs_to_delete = [blob.name for blob in self.connection.list_blobs(container_name, prefix=blob_name, **kwargs)]
    elif self.check_for_blob(container_name, blob_name):
        blobs_to_delete = [blob_name]
    else:
        blobs_to_delete = []
    if not ignore_if_missing and len(blobs_to_delete) == 0:
        raise AirflowException('Blob(s) not found: {}'.format(blob_name))
    for blob_uri in blobs_to_delete:
        self.log.info('Deleting blob: ' + blob_uri)
        self.connection.delete_blob(container_name, blob_uri, delete_snapshots='include', **kwargs)