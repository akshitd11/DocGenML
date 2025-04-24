def sina_download(url, output_dir='.', merge=True, info_only=False, **kwargs):
    if 'news.sina.com.cn/zxt' in url:
        sina_zxt(url, output_dir=output_dir, merge=merge, info_only=info_only, **kwargs)
        return
    vid = match1(url, 'vid=(\\d+)')
    if vid is None:
        video_page = get_content(url)
        vid = hd_vid = match1(video_page, "hd_vid\\s*:\\s*\\'([^\\']+)\\'")
        if hd_vid == '0':
            vids = match1(video_page, "[^\\w]vid\\s*:\\s*\\'([^\\']+)\\'").split('|')
            vid = vids[-1]
    if vid is None:
        vid = match1(video_page, 'vid:"?(\\d+)"?')
    if vid:
        sina_download_by_vid(vid, output_dir=output_dir, merge=merge, info_only=info_only)
    else:
        vkey = match1(video_page, 'vkey\\s*:\\s*"([^"]+)"')
        if vkey is None:
            vid = match1(url, '#(\\d+)')
            sina_download_by_vid(vid, output_dir=output_dir, merge=merge, info_only=info_only)
            return
        title = match1(video_page, 'title\\s*:\\s*"([^"]+)"')
        sina_download_by_vkey(vkey, title=title, output_dir=output_dir, merge=merge, info_only=info_only)