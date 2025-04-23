def poke(self, context):
    sb = self.hook(self.hdfs_conn_id).get_conn()
    self.log.info('Poking for %s to be a directory with files matching %s', self.filepath, self.regex.pattern)
    result = [f for f in sb.ls([self.filepath], include_toplevel=False) if f['file_type'] == 'f' and self.regex.match(f['path'].replace('%s/' % self.filepath, ''))]
    result = self.filter_for_ignored_ext(result, self.ignored_ext, self.ignore_copying)
    result = self.filter_for_filesize(result, self.file_size)
    return bool(result)