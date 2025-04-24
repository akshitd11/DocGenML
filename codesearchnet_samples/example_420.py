def _write_local_data_files(self, cursor):
    schema = list(map(lambda schema_tuple: schema_tuple[0].replace(' ', '_'), cursor.description))
    file_no = 0
    tmp_file_handle = NamedTemporaryFile(delete=True)
    tmp_file_handles = {self.filename.format(file_no): tmp_file_handle}
    for row in cursor:
        row = map(self.convert_types, row)
        row_dict = dict(zip(schema, row))
        s = json.dumps(row_dict, sort_keys=True)
        s = s.encode('utf-8')
        tmp_file_handle.write(s)
        tmp_file_handle.write(b'\n')
        if tmp_file_handle.tell() >= self.approx_max_file_size_bytes:
            file_no += 1
            tmp_file_handle = NamedTemporaryFile(delete=True)
            tmp_file_handles[self.filename.format(file_no)] = tmp_file_handle
    return tmp_file_handles