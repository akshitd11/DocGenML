def load_bytes(self, bytes_data, key, bucket_name=None, replace=False, encrypt=False):
    if not bucket_name:
        (bucket_name, key) = self.parse_s3_url(key)
    if not replace and self.check_for_key(key, bucket_name):
        raise ValueError('The key {key} already exists.'.format(key=key))
    extra_args = {}
    if encrypt:
        extra_args['ServerSideEncryption'] = 'AES256'
    filelike_buffer = BytesIO(bytes_data)
    client = self.get_conn()
    client.upload_fileobj(filelike_buffer, bucket_name, key, ExtraArgs=extra_args)