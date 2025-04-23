def correct_maybe_zipped(fileloc):
    (_, archive, filename) = re.search('((.*\\.zip){})?(.*)'.format(re.escape(os.sep)), fileloc).groups()
    if archive and zipfile.is_zipfile(archive):
        return archive
    else:
        return fileloc