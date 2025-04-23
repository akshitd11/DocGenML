def miaopai_download_by_fid(fid, output_dir='.', merge=False, info_only=False, **kwargs):
    page_url = 'http://video.weibo.com/show?fid=' + fid + '&type=mp4'
    mobile_page = get_content(page_url, headers=fake_headers_mobile)
    url = match1(mobile_page, '<video id=.*?src=[\\\'"](.*?)[\\\'"]\\W')
    if url is None:
        wb_mp = re.search('<script src=([\\\'"])(.+?wb_mp\\.js)\\1>', mobile_page).group(2)
        return miaopai_download_by_wbmp(wb_mp, fid, output_dir=output_dir, merge=merge, info_only=info_only, total_size=None, **kwargs)
    title = match1(mobile_page, '<title>((.|\\n)+?)</title>')
    if not title:
        title = fid
    title = title.replace('\n', '_')
    (ext, size) = ('mp4', url_info(url)[2])
    print_info(site_info, title, ext, size)
    if not info_only:
        download_urls([url], title, ext, total_size=None, output_dir=output_dir, merge=merge)