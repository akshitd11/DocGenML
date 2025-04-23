def list_prefixes(self, bucket_name, prefix='', delimiter='', page_size=None, max_items=None):
    config = {'PageSize': page_size, 'MaxItems': max_items}
    paginator = self.get_conn().get_paginator('list_objects_v2')
    response = paginator.paginate(Bucket=bucket_name, Prefix=prefix, Delimiter=delimiter, PaginationConfig=config)
    has_results = False
    prefixes = []
    for page in response:
        if 'CommonPrefixes' in page:
            has_results = True
            for p in page['CommonPrefixes']:
                prefixes.append(p['Prefix'])
    if has_results:
        return prefixes