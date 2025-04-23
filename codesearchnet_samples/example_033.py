def cbs_download(url, output_dir='.', merge=True, info_only=False, **kwargs):
    html = get_content(url)
    pid = match1(html, "video\\.settings\\.pid\\s*=\\s*\\'([^\\']+)\\'")
    title = match1(html, 'video\\.settings\\.title\\s*=\\s*\\"([^\\"]+)\\"')
    theplatform_download_by_pid(pid, title, output_dir=output_dir, merge=merge, info_only=info_only)