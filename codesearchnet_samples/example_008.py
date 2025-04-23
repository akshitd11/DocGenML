def ucas_download_playlist(url, output_dir='.', merge=False, info_only=False, **kwargs):
    html = get_content(url)
    parts = re.findall('(getplaytitle.do\\?.+)"', html)
    assert parts, 'No part found!'
    for part_path in parts:
        ucas_download('http://v.ucas.ac.cn/course/' + part_path, output_dir=output_dir, merge=merge, info_only=info_only)