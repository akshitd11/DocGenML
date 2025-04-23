def describe_directory(self, path):
    conn = self.get_conn()
    conn.cwd(path)
    try:
        files = dict(conn.mlsd())
    except AttributeError:
        files = dict(mlsd(conn))
    return files