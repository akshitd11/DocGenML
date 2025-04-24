def mlsd(conn, path='', facts=None):
    facts = facts or []
    if facts:
        conn.sendcmd('OPTS MLST ' + ';'.join(facts) + ';')
    if path:
        cmd = 'MLSD %s' % path
    else:
        cmd = 'MLSD'
    lines = []
    conn.retrlines(cmd, lines.append)
    for line in lines:
        (facts_found, _, name) = line.rstrip(ftplib.CRLF).partition(' ')
        entry = {}
        for fact in facts_found[:-1].split(';'):
            (key, _, value) = fact.partition('=')
            entry[key.lower()] = value
        yield (name, entry)