def bulk_load(self, table, tmp_file):
    conn = self.get_conn()
    cur = conn.cursor()
    cur.execute("\n            LOAD DATA LOCAL INFILE '{tmp_file}'\n            INTO TABLE {table}\n            ".format(tmp_file=tmp_file, table=table))
    conn.commit()