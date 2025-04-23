def execute(self, context):
    hook = GoogleCloudStorageHook(google_cloud_storage_conn_id=self.google_cloud_storage_conn_id, delegate_to=self.delegate_to)
    hook.upload(bucket_name=self.bucket, object_name=self.dst, mime_type=self.mime_type, filename=self.src, gzip=self.gzip)