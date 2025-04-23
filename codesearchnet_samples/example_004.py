def fc2video_download(url, output_dir='.', merge=True, info_only=False, **kwargs):
    hostname = urlparse(url).hostname
    if not ('fc2.com' in hostname or 'xiaojiadianvideo.asia' in hostname):
        return False
    upid = match1(url, '.+/content/(\\w+)')
    fc2video_download_by_upid(upid, output_dir, merge, info_only)