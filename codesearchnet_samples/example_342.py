def poke(self, context):
    sb = self.hook(self.hdfs_conn_id).get_conn()
    result = [f for f in sb.ls([self.filepath], include_toplevel=True)]
    result = self.filter_for_ignored_ext(result, self.ignored_ext, self.ignore_copying)
    result = self.filter_for_filesize(result, self.file_size)
    if self.be_empty:
        self.log.info('Poking for filepath %s to a empty directory', self.filepath)
        return len(result) == 1 and result[0]['path'] == self.filepath
    else:
        self.log.info('Poking for filepath %s to a non empty directory', self.filepath)
        result.pop(0)
        return bool(result) and result[0]['file_type'] == 'f'