def get_content(url, headers={}, decoded=True):
    logging.debug('get_content: %s' % url)
    req = request.Request(url, headers=headers)
    if cookies:
        cookies.add_cookie_header(req)
        req.headers.update(req.unredirected_hdrs)
    response = urlopen_with_retry(req)
    data = response.read()
    content_encoding = response.getheader('Content-Encoding')
    if content_encoding == 'gzip':
        data = ungzip(data)
    elif content_encoding == 'deflate':
        data = undeflate(data)
    if decoded:
        charset = match1(response.getheader('Content-Type', ''), 'charset=([\\w-]+)')
        if charset is not None:
            data = data.decode(charset, 'ignore')
        else:
            data = data.decode('utf-8', 'ignore')
    return data