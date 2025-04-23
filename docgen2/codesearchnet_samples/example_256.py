def reap_process_group(pid, log, sig=signal.SIGTERM, timeout=DEFAULT_TIME_TO_WAIT_AFTER_SIGTERM):

    def on_terminate(p):
        log.info('Process %s (%s) terminated with exit code %s', p, p.pid, p.returncode)
    if pid == os.getpid():
        raise RuntimeError('I refuse to kill myself')
    parent = psutil.Process(pid)
    children = parent.children(recursive=True)
    children.append(parent)
    try:
        pg = os.getpgid(pid)
    except OSError as err:
        if err.errno == errno.ESRCH:
            return
        raise
    log.info('Sending %s to GPID %s', sig, pg)
    os.killpg(os.getpgid(pid), sig)
    (gone, alive) = psutil.wait_procs(children, timeout=timeout, callback=on_terminate)
    if alive:
        for p in alive:
            log.warn('process %s (%s) did not respond to SIGTERM. Trying SIGKILL', p, pid)
        os.killpg(os.getpgid(pid), signal.SIGKILL)
        (gone, alive) = psutil.wait_procs(alive, timeout=timeout, callback=on_terminate)
        if alive:
            for p in alive:
                log.error('Process %s (%s) could not be killed. Giving up.', p, p.pid)