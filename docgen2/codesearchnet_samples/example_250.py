def detect_conf_var():
    ticket_cache = configuration.conf.get('kerberos', 'ccache')
    with open(ticket_cache, 'rb') as f:
        return b'X-CACHECONF:' in f.read()