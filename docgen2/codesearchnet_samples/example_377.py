def check_for_bucket(self, bucket_name):
    try:
        self.get_conn().head_bucket(Bucket=bucket_name)
        return True
    except ClientError as e:
        self.log.info(e.response['Error']['Message'])
        return False