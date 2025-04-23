def print_more_compatible(*args, **kwargs):
    import builtins as __builtin__
    "Overload default print function as py (<3.3) does not support 'flush' keyword.\n    Although the function name can be same as print to get itself overloaded automatically,\n    I'd rather leave it with a different name and only overload it when importing to make less confusion.\n    "
    if sys.version_info[:2] >= (3, 3):
        return __builtin__.print(*args, **kwargs)
    doFlush = kwargs.pop('flush', False)
    ret = __builtin__.print(*args, **kwargs)
    if doFlush:
        kwargs.get('file', sys.stdout).flush()
    return ret