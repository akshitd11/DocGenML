def datetime(*args, **kwargs):
    if 'tzinfo' not in kwargs:
        kwargs['tzinfo'] = TIMEZONE
    return dt.datetime(*args, **kwargs)