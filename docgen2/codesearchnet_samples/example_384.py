def read_key(self, key, bucket_name=None):
    obj = self.get_key(key, bucket_name)
    return obj.get()['Body'].read().decode('utf-8')