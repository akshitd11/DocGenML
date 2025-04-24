def write_object_to_file(self, query_results, filename, fmt='csv', coerce_to_timestamp=False, record_time_added=False):
    fmt = fmt.lower()
    if fmt not in ['csv', 'json', 'ndjson']:
        raise ValueError('Format value is not recognized: {}'.format(fmt))
    df = pd.DataFrame.from_records(query_results, exclude=['attributes'])
    df.columns = [column.lower() for column in df.columns]
    if coerce_to_timestamp and df.shape[0] > 0:
        object_name = query_results[0]['attributes']['type']
        self.log.info('Coercing timestamps for: %s', object_name)
        schema = self.describe_object(object_name)
        possible_timestamp_cols = [field['name'].lower() for field in schema['fields'] if field['type'] in ['date', 'datetime'] and field['name'].lower() in df.columns]
        df[possible_timestamp_cols] = df[possible_timestamp_cols].apply(self._to_timestamp)
    if record_time_added:
        fetched_time = time.time()
        df['time_fetched_from_salesforce'] = fetched_time
    if fmt == 'csv':
        self.log.info('Cleaning data and writing to CSV')
        possible_strings = df.columns[df.dtypes == 'object']
        df[possible_strings] = df[possible_strings].apply(lambda x: x.str.replace('\r\n', '').str.replace('\n', ''))
        df.to_csv(filename, index=False)
    elif fmt == 'json':
        df.to_json(filename, 'records', date_unit='s')
    elif fmt == 'ndjson':
        df.to_json(filename, 'records', lines=True, date_unit='s')
    return df