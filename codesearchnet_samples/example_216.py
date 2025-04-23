def _strip_unsafe_kubernetes_special_chars(string):
    return ''.join((ch.lower() for (ind, ch) in enumerate(string) if ch.isalnum()))