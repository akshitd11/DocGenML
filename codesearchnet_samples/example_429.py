def _parse_host(host):
    urlparse_host = urlparse.urlparse(host).hostname
    if urlparse_host:
        return urlparse_host
    else:
        return host