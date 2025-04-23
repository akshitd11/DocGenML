def uncompress_file(input_file_name, file_extension, dest_dir):
    if file_extension.lower() not in ('.gz', '.bz2'):
        raise NotImplementedError('Received {} format. Only gz and bz2 files can currently be uncompressed.'.format(file_extension))
    if file_extension.lower() == '.gz':
        fmodule = gzip.GzipFile
    elif file_extension.lower() == '.bz2':
        fmodule = bz2.BZ2File
    with fmodule(input_file_name, mode='rb') as f_compressed, NamedTemporaryFile(dir=dest_dir, mode='wb', delete=False) as f_uncompressed:
        shutil.copyfileobj(f_compressed, f_uncompressed)
    return f_uncompressed.name