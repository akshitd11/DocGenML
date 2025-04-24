def on_pre_execution(**kwargs):
    logging.debug('Calling callbacks: %s', __pre_exec_callbacks)
    for cb in __pre_exec_callbacks:
        try:
            cb(**kwargs)
        except Exception:
            logging.exception('Failed on pre-execution callback using %s', cb)