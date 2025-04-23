def _make_safe_label_value(string):
    MAX_LABEL_LEN = 63
    safe_label = re.sub('^[^a-z0-9A-Z]*|[^a-zA-Z0-9_\\-\\.]|[^a-z0-9A-Z]*$', '', string)
    if len(safe_label) > MAX_LABEL_LEN or string != safe_label:
        safe_hash = hashlib.md5(string.encode()).hexdigest()[:9]
        safe_label = safe_label[:MAX_LABEL_LEN - len(safe_hash) - 1] + '-' + safe_hash
    return safe_label