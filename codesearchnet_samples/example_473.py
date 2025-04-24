def list_directory(self, path, nlst=False):
    conn = self.get_conn()
    conn.cwd(path)
    files = conn.nlst()
    return files