def ucas_download_single(url, output_dir='.', merge=False, info_only=False, **kwargs):
    html = get_content(url)
    resourceID = re.findall('resourceID":"([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})', html)[0]
    assert resourceID != '', 'Cannot find resourceID!'
    title = match1(html, '<div class="bc-h">(.+)</div>')
    url_lists = _ucas_get_url_lists_by_resourceID(resourceID)
    assert url_lists, 'Cannot find any URL of such class!'
    for (k, part) in enumerate(url_lists):
        part_title = title + '_' + str(k)
        print_info(site_info, part_title, 'flv', 0)
        if not info_only:
            download_urls(part, part_title, 'flv', total_size=None, output_dir=output_dir, merge=merge)