def copy_object(self, source_bucket_key, dest_bucket_key, source_bucket_name=None, dest_bucket_name=None, source_version_id=None):
    if dest_bucket_name is None:
        (dest_bucket_name, dest_bucket_key) = self.parse_s3_url(dest_bucket_key)
    else:
        parsed_url = urlparse(dest_bucket_key)
        if parsed_url.scheme != '' or parsed_url.netloc != '':
            raise AirflowException('If dest_bucket_name is provided, ' + 'dest_bucket_key should be relative path ' + 'from root level, rather than a full s3:// url')
    if source_bucket_name is None:
        (source_bucket_name, source_bucket_key) = self.parse_s3_url(source_bucket_key)
    else:
        parsed_url = urlparse(source_bucket_key)
        if parsed_url.scheme != '' or parsed_url.netloc != '':
            raise AirflowException('If source_bucket_name is provided, ' + 'source_bucket_key should be relative path ' + 'from root level, rather than a full s3:// url')
    CopySource = {'Bucket': source_bucket_name, 'Key': source_bucket_key, 'VersionId': source_version_id}
    response = self.get_conn().copy_object(Bucket=dest_bucket_name, Key=dest_bucket_key, CopySource=CopySource)
    return response