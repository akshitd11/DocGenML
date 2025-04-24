def pprinttable(rows):
    if not rows:
        return
    if hasattr(rows[0], '_fields'):
        headers = rows[0]._fields
    else:
        headers = ['col{}'.format(i) for i in range(len(rows[0]))]
    lens = [len(s) for s in headers]
    for row in rows:
        for i in range(len(rows[0])):
            slenght = len('{}'.format(row[i]))
            if slenght > lens[i]:
                lens[i] = slenght
    formats = []
    hformats = []
    for i in range(len(rows[0])):
        if isinstance(rows[0][i], int):
            formats.append('%%%dd' % lens[i])
        else:
            formats.append('%%-%ds' % lens[i])
        hformats.append('%%-%ds' % lens[i])
    pattern = ' | '.join(formats)
    hpattern = ' | '.join(hformats)
    separator = '-+-'.join(['-' * n for n in lens])
    s = ''
    s += separator + '\n'
    s += hpattern % tuple(headers) + '\n'
    s += separator + '\n'

    def f(t):
        return '{}'.format(t) if isinstance(t, basestring) else t
    for line in rows:
        s += pattern % tuple((f(t) for t in line)) + '\n'
    s += separator + '\n'
    return s