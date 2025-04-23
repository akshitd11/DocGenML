def vimeo_download_by_channel(url, output_dir='.', merge=False, info_only=False, **kwargs):
    channel_id = match1(url, 'http://vimeo.com/channels/(\\w+)')
    vimeo_download_by_channel_id(channel_id, output_dir, merge, info_only, **kwargs)