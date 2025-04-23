def download_by_id(self, vid='', title=None, output_dir='.', merge=True, info_only=False, **kwargs):
    assert vid
    self.prepare(vid=vid, title=title, **kwargs)
    self.extract(**kwargs)
    self.download(output_dir=output_dir, merge=merge, info_only=info_only, **kwargs)