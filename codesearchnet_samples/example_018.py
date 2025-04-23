def print_log(text, *colors):
    sys.stderr.write(sprint('{}: {}'.format(script_name, text), *colors) + '\n')