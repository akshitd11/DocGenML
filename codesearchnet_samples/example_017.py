def sprint(text, *colors):
    return '\x1b[{}m{content}\x1b[{}m'.format(';'.join([str(color) for color in colors]), RESET, content=text) if IS_ANSI_TERMINAL and colors else text