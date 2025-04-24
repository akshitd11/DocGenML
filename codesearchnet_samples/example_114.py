def utcnow():
    d = dt.datetime.utcnow()
    d = d.replace(tzinfo=utc)
    return d