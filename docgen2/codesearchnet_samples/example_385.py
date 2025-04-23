def select_key(self, key, bucket_name=None, expression='SELECT * FROM S3Object', expression_type='SQL', input_serialization=None, output_serialization=None):
    if input_serialization is None:
        input_serialization = {'CSV': {}}
    if output_serialization is None:
        output_serialization = {'CSV': {}}
    if not bucket_name:
        (bucket_name, key) = self.parse_s3_url(key)
    response = self.get_conn().select_object_content(Bucket=bucket_name, Key=key, Expression=expression, ExpressionType=expression_type, InputSerialization=input_serialization, OutputSerialization=output_serialization)
    return ''.join((event['Records']['Payload'].decode('utf-8') for event in response['Payload'] if 'Records' in event))