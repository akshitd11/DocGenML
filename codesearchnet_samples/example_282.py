def get_default_executor():
    global DEFAULT_EXECUTOR
    if DEFAULT_EXECUTOR is not None:
        return DEFAULT_EXECUTOR
    executor_name = configuration.conf.get('core', 'EXECUTOR')
    DEFAULT_EXECUTOR = _get_executor(executor_name)
    log = LoggingMixin().log
    log.info('Using executor %s', executor_name)
    return DEFAULT_EXECUTOR