def check_for_key(self, key, bucket_name=None):
    if not bucket_name:
        (bucket_name, key) = self.parse_s3_url(key)
    try:
        self.get_conn().head_object(Bucket=bucket_name, Key=key)
        return True
    except ClientError as e:
        self.log.info(e.response['Error']['Message'])
        return False