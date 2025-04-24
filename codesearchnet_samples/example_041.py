def ungzip(data):
    from io import BytesIO
    import gzip
    buffer = BytesIO(data)
    f = gzip.GzipFile(fileobj=buffer)
    return f.read()