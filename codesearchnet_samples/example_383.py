def get_key(self, key, bucket_name=None):
    if not bucket_name:
        (bucket_name, key) = self.parse_s3_url(key)
    obj = self.get_resource_type('s3').Object(bucket_name, key)
    obj.load()
    return obj