def get_mgtv_real_url(url):
    content = loads(get_content(url))
    m3u_url = content['info']
    split = urlsplit(m3u_url)
    base_url = '{scheme}://{netloc}{path}/'.format(scheme=split[0], netloc=split[1], path=dirname(split[2]))
    content = get_content(content['info'])
    segment_list = []
    segments_size = 0
    for i in content.split():
        if not i.startswith('#'):
            segment_list.append(base_url + i)
        elif i.startswith('#EXT-MGTV-File-SIZE:'):
            segments_size += int(i[i.rfind(':') + 1:])
    return (m3u_url, segments_size, segment_list)