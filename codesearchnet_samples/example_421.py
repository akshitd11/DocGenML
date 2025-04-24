def _upload_to_gcs(self, files_to_upload):
    hook = GoogleCloudStorageHook(google_cloud_storage_conn_id=self.google_cloud_storage_conn_id, delegate_to=self.delegate_to)
    for (object_name, tmp_file_handle) in files_to_upload.items():
        hook.upload(self.bucket, object_name, tmp_file_handle.name, 'application/json', self.gzip if object_name != self.schema_filename else False)