def reduce_in_chunks(fn, iterable, initializer, chunk_size=0):
    if len(iterable) == 0:
        return initializer
    if chunk_size == 0:
        chunk_size = len(iterable)
    return reduce(fn, chunks(iterable, chunk_size), initializer)