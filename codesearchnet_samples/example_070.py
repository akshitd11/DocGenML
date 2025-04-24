def sigquit_handler(sig, frame):
    print('Dumping stack traces for all threads in PID {}'.format(os.getpid()))
    id_to_name = dict([(th.ident, th.name) for th in threading.enumerate()])
    code = []
    for (thread_id, stack) in sys._current_frames().items():
        code.append('\n# Thread: {}({})'.format(id_to_name.get(thread_id, ''), thread_id))
        for (filename, line_number, name, line) in traceback.extract_stack(stack):
            code.append('File: "{}", line {}, in {}'.format(filename, line_number, name))
            if line:
                code.append('  {}'.format(line.strip()))
    print('\n'.join(code))