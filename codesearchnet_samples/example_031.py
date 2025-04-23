def legitimize(text, os=detect_os()):
    text = text.translate({0: None, ord('/'): '-', ord('|'): '-'})
    if os == 'windows' or os == 'cygwin' or os == 'wsl':
        text = text.translate({ord(':'): '-', ord('*'): '-', ord('?'): '-', ord('\\'): '-', ord('"'): "'", ord('+'): '-', ord('<'): '-', ord('>'): '-', ord('['): '(', ord(']'): ')', ord('\t'): ' '})
    else:
        if os == 'mac':
            text = text.translate({ord(':'): '-'})
        if text.startswith('.'):
            text = text[1:]
    text = text[:80]
    return text