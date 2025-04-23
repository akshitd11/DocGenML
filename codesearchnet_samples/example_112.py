def mkdirs(path, mode):
    try:
        o_umask = os.umask(0)
        os.makedirs(path, mode)
    except OSError:
        if not os.path.isdir(path):
            raise
    finally:
        os.umask(o_umask)