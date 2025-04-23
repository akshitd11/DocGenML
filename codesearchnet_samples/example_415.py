def list(self, path):
    if '*' in path:
        return self.connection.glob(path)
    else:
        return self.connection.walk(path)