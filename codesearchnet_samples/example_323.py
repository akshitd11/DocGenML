def on_post_execution(**kwargs):
    logging.debug('Calling callbacks: %s', __post_exec_callbacks)
    for cb in __post_exec_callbacks:
        try:
            cb(**kwargs)
        except Exception:
            logging.exception('Failed on post-execution callback using %s', cb)