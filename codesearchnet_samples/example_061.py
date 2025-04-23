def bulk_load(self, table, tmp_file):
    self.copy_expert('COPY {table} FROM STDIN'.format(table=table), tmp_file)