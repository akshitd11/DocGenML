def list_keys(self, bucket_name, prefix='', delimiter='', page_size=None, max_items=None):
    config = {'PageSize': page_size, 'MaxItems': max_items}
    paginator = self.get_conn().get_paginator('list_objects_v2')
    response = paginator.paginate(Bucket=bucket_name, Prefix=prefix, Delimiter=delimiter, PaginationConfig=config)
    has_results = False
    keys = []
    for page in response:
        if 'Contents' in page:
            has_results = True
            for k in page['Contents']:
                keys.append(k['Key'])
    if has_results:
        return keys