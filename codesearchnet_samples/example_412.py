def check_for_file(self, file_path):
    try:
        files = self.connection.glob(file_path, details=False, invalidate_cache=True)
        return len(files) == 1
    except FileNotFoundError:
        return False