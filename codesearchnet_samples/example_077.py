def restart_workers(gunicorn_master_proc, num_workers_expected, master_timeout):

    def wait_until_true(fn, timeout=0):
        """
        Sleeps until fn is true
        """
        t = time.time()
        while not fn():
            if 0 < timeout <= time.time() - t:
                raise AirflowWebServerTimeout('No response from gunicorn master within {0} seconds'.format(timeout))
            time.sleep(0.1)

    def start_refresh(gunicorn_master_proc):
        batch_size = conf.getint('webserver', 'worker_refresh_batch_size')
        log.debug('%s doing a refresh of %s workers', state, batch_size)
        sys.stdout.flush()
        sys.stderr.flush()
        excess = 0
        for _ in range(batch_size):
            gunicorn_master_proc.send_signal(signal.SIGTTIN)
            excess += 1
            wait_until_true(lambda : num_workers_expected + excess == get_num_workers_running(gunicorn_master_proc), master_timeout)
    try:
        wait_until_true(lambda : num_workers_expected == get_num_workers_running(gunicorn_master_proc), master_timeout)
        while True:
            num_workers_running = get_num_workers_running(gunicorn_master_proc)
            num_ready_workers_running = get_num_ready_workers_running(gunicorn_master_proc)
            state = '[{0} / {1}]'.format(num_ready_workers_running, num_workers_running)
            if num_ready_workers_running < num_workers_running:
                log.debug('%s some workers are starting up, waiting...', state)
                sys.stdout.flush()
                time.sleep(1)
            elif num_workers_running > num_workers_expected:
                excess = num_workers_running - num_workers_expected
                log.debug('%s killing %s workers', state, excess)
                for _ in range(excess):
                    gunicorn_master_proc.send_signal(signal.SIGTTOU)
                    excess -= 1
                    wait_until_true(lambda : num_workers_expected + excess == get_num_workers_running(gunicorn_master_proc), master_timeout)
            elif num_workers_running == num_workers_expected:
                refresh_interval = conf.getint('webserver', 'worker_refresh_interval')
                log.debug('%s sleeping for %ss starting doing a refresh...', state, refresh_interval)
                time.sleep(refresh_interval)
                start_refresh(gunicorn_master_proc)
            else:
                log.error('%s some workers seem to have died and gunicorndid not restart them as expected', state)
                time.sleep(10)
                if len(psutil.Process(gunicorn_master_proc.pid).children()) < num_workers_expected:
                    start_refresh(gunicorn_master_proc)
    except (AirflowWebServerTimeout, OSError) as err:
        log.error(err)
        log.error('Shutting down webserver')
        try:
            gunicorn_master_proc.terminate()
            gunicorn_master_proc.wait()
        finally:
            sys.exit(1)