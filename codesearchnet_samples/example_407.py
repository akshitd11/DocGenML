def _init_file(self, ti):
    relative_path = self._render_filename(ti, ti.try_number)
    full_path = os.path.join(self.local_base, relative_path)
    directory = os.path.dirname(full_path)
    if not os.path.exists(directory):
        mkdirs(directory, 511)
    if not os.path.exists(full_path):
        open(full_path, 'a').close()
        os.chmod(full_path, 438)
    return full_path