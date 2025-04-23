def makeMimi(upid):
    strSeed = 'gGddgPfeaf_gzyr'
    prehash = upid + '_' + strSeed
    return md5(prehash.encode('utf-8')).hexdigest()