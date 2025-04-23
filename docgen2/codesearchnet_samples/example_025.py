def vimeo_download_by_id(id, title=None, output_dir='.', merge=True, info_only=False, **kwargs):
    site = VimeoExtractor()
    site.download_by_vid(id, info_only=info_only, output_dir=output_dir, merge=merge, **kwargs)