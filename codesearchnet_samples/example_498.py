def set_context(self, filename):
    local_loc = self._init_file(filename)
    self.handler = logging.FileHandler(local_loc)
    self.handler.setFormatter(self.formatter)
    self.handler.setLevel(self.level)
    if self._cur_date < datetime.today():
        self._symlink_latest_log_directory()
        self._cur_date = datetime.today()