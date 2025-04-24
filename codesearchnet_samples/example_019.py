def e(message, exit_code=None):
    print_log(message, YELLOW, BOLD)
    if exit_code is not None:
        sys.exit(exit_code)