def yixia_download(url, output_dir='.', merge=True, info_only=False, **kwargs):
    hostname = urlparse(url).hostname
    if 'n.miaopai.com' == hostname:
        smid = match1(url, 'n\\.miaopai\\.com/media/([^.]+)')
        miaopai_download_by_smid(smid, output_dir, merge, info_only)
        return
    elif 'miaopai.com' in hostname:
        yixia_download_by_scid = yixia_miaopai_download_by_scid
        site_info = 'Yixia Miaopai'
        scid = match1(url, 'miaopai\\.com/show/channel/([^.]+)\\.htm') or match1(url, 'miaopai\\.com/show/([^.]+)\\.htm') or match1(url, 'm\\.miaopai\\.com/show/channel/([^.]+)\\.htm') or match1(url, 'm\\.miaopai\\.com/show/channel/([^.]+)')
    elif 'xiaokaxiu.com' in hostname:
        yixia_download_by_scid = yixia_xiaokaxiu_download_by_scid
        site_info = 'Yixia Xiaokaxiu'
        if re.match('http://v.xiaokaxiu.com/v/.+\\.html', url):
            scid = match1(url, 'http://v.xiaokaxiu.com/v/(.+)\\.html')
        elif re.match('http://m.xiaokaxiu.com/m/.+\\.html', url):
            scid = match1(url, 'http://m.xiaokaxiu.com/m/(.+)\\.html')
    else:
        pass
    yixia_download_by_scid(scid, output_dir, merge, info_only)