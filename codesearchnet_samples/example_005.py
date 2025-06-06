def dailymotion_download(url, output_dir='.', merge=True, info_only=False, **kwargs):
    html = get_content(rebuilt_url(url))
    info = json.loads(match1(html, 'qualities":({.+?}),"'))
    title = match1(html, '"video_title"\\s*:\\s*"([^"]+)"') or match1(html, '"title"\\s*:\\s*"([^"]+)"')
    title = unicodize(title)
    for quality in ['1080', '720', '480', '380', '240', '144', 'auto']:
        try:
            real_url = info[quality][1]['url']
            if real_url:
                break
        except KeyError:
            pass
    (mime, ext, size) = url_info(real_url)
    print_info(site_info, title, mime, size)
    if not info_only:
        download_urls([real_url], title, ext, size, output_dir=output_dir, merge=merge)