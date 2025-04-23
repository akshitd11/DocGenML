def post_content(url, headers={}, post_data={}, decoded=True, **kwargs):
    if kwargs.get('post_data_raw'):
        logging.debug('post_content: %s\npost_data_raw: %s' % (url, kwargs['post_data_raw']))
    else:
        logging.debug('post_content: %s\npost_data: %s' % (url, post_data))
    req = request.Request(url, headers=headers)
    if cookies:
        cookies.add_cookie_header(req)
        req.headers.update(req.unredirected_hdrs)
    if kwargs.get('post_data_raw'):
        post_data_enc = bytes(kwargs['post_data_raw'], 'utf-8')
    else:
        post_data_enc = bytes(parse.urlencode(post_data), 'utf-8')
    response = urlopen_with_retry(req, data=post_data_enc)
    data = response.read()
    content_encoding = response.getheader('Content-Encoding')
    if content_encoding == 'gzip':
        data = ungzip(data)
    elif content_encoding == 'deflate':
        data = undeflate(data)
    if decoded:
        charset = match1(response.getheader('Content-Type'), 'charset=([\\w-]+)')
        if charset is not None:
            data = data.decode(charset)
        else:
            data = data.decode('utf-8')
    return data