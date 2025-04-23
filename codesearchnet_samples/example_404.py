def set_context(self, ti):
    local_loc = self._init_file(ti)
    self.handler = logging.FileHandler(local_loc)
    self.handler.setFormatter(self.formatter)
    self.handler.setLevel(self.level)