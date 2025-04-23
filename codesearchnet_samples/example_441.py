def parse_gcs_url(gsurl):
    parsed_url = urlparse(gsurl)
    if not parsed_url.netloc:
        raise AirflowException('Please provide a bucket name')
    else:
        bucket = parsed_url.netloc
        blob = parsed_url.path.strip('/')
        return (bucket, blob)