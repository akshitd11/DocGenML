def veoh_download(url, output_dir='.', merge=False, info_only=False, **kwargs):
    if re.match('http://www.veoh.com/watch/\\w+', url):
        item_id = match1(url, 'http://www.veoh.com/watch/(\\w+)')
    elif re.match('http://www.veoh.com/m/watch.php\\?v=\\.*', url):
        item_id = match1(url, 'http://www.veoh.com/m/watch.php\\?v=(\\w+)')
    else:
        raise NotImplementedError('Cannot find item ID')
    veoh_download_by_id(item_id, output_dir='.', merge=False, info_only=info_only, **kwargs)