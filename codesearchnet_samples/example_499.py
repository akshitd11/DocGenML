def _init_file(self, filename):
    relative_path = self._render_filename(filename)
    full_path = os.path.join(self._get_log_directory(), relative_path)
    directory = os.path.dirname(full_path)
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError:
            if not os.path.isdir(directory):
                raise
    if not os.path.exists(full_path):
        open(full_path, 'a').close()
    return full_path