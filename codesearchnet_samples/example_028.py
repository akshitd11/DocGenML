def get_vid_from_url(url):
    vid = match1(url, 'https?://www.mgtv.com/(?:b|l)/\\d+/(\\d+).html')
    if not vid:
        vid = match1(url, 'https?://www.mgtv.com/hz/bdpz/\\d+/(\\d+).html')
    return vid