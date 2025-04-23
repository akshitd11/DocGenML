def create_bucket(self, bucket_name, region_name=None):
    s3_conn = self.get_conn()
    if not region_name:
        region_name = s3_conn.meta.region_name
    if region_name == 'us-east-1':
        self.get_conn().create_bucket(Bucket=bucket_name)
    else:
        self.get_conn().create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region_name})