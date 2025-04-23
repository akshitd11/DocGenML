def utc_epoch():
    d = dt.datetime(1970, 1, 1)
    d = d.replace(tzinfo=utc)
    return d