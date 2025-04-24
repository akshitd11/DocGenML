def bulk_dump(self, table, tmp_file):
    self.copy_expert('COPY {table} TO STDOUT'.format(table=table), tmp_file)