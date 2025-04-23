def ckplayer_get_info_by_xml(ckinfo):
    e = ET.XML(ckinfo)
    video_dict = {'title': '', 'links': [], 'size': 0, 'flashvars': ''}
    dictified = dictify(e)['ckplayer']
    if 'info' in dictified:
        if '_text' in dictified['info'][0]['title'][0]:
            video_dict['title'] = dictified['info'][0]['title'][0]['_text'].strip()
    if '_text' in dictified['video'][0]['size'][0]:
        video_dict['size'] = sum([int(i['size'][0]['_text']) for i in dictified['video']])
    if '_text' in dictified['video'][0]['file'][0]:
        video_dict['links'] = [i['file'][0]['_text'].strip() for i in dictified['video']]
    if '_text' in dictified['flashvars'][0]:
        video_dict['flashvars'] = dictified['flashvars'][0]['_text'].strip()
    return video_dict