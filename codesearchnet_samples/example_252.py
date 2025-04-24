def chunks(items, chunk_size):
    if chunk_size <= 0:
        raise ValueError('Chunk size must be a positive integer')
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]