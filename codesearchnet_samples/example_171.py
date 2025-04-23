def set_context(logger, value):
    _logger = logger
    while _logger:
        for handler in _logger.handlers:
            try:
                handler.set_context(value)
            except AttributeError:
                pass
        if _logger.propagate is True:
            _logger = _logger.parent
        else:
            _logger = None