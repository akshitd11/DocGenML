def wtf(message, exit_code=1):
    print_log(message, RED, BOLD)
    if exit_code is not None:
        sys.exit(exit_code)