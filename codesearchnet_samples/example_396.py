def _write_local_schema_file(self, cursor):
    schema = []
    tmp_schema_file_handle = NamedTemporaryFile(delete=True)
    for (name, type) in zip(cursor.column_names, cursor.column_types):
        schema.append(self.generate_schema_dict(name, type))
    json_serialized_schema = json.dumps(schema).encode('utf-8')
    tmp_schema_file_handle.write(json_serialized_schema)
    return {self.schema_filename: tmp_schema_file_handle}