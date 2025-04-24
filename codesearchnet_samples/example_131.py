def execute(self, context):
    hook = WasbHook(wasb_conn_id=self.wasb_conn_id)
    self.log.info('Uploading %s to wasb://%s as %s'.format(self.file_path, self.container_name, self.blob_name))
    hook.load_file(self.file_path, self.container_name, self.blob_name, **self.load_options)