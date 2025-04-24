def copy_expert(self, sql, filename, open=open):
    if not os.path.isfile(filename):
        with open(filename, 'w'):
            pass
    with open(filename, 'r+') as f:
        with closing(self.get_conn()) as conn:
            with closing(conn.cursor()) as cur:
                cur.copy_expert(sql, f)
                f.truncate(f.tell())
                conn.commit()