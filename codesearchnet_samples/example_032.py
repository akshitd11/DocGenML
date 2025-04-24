def get_terminal_size():
    try:
        import fcntl, termios, struct
        return struct.unpack('hh', fcntl.ioctl(1, termios.TIOCGWINSZ, '1234'))
    except:
        return (40, 80)