def action_logging(f):

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        """
        An wrapper for cli functions. It assumes to have Namespace instance
        at 1st positional argument
        :param args: Positional argument. It assumes to have Namespace instance
        at 1st positional argument
        :param kwargs: A passthrough keyword argument
        """
        assert args
        assert isinstance(args[0], Namespace), '1st positional argument should be argparse.Namespace instance, but {}'.format(args[0])
        metrics = _build_metrics(f.__name__, args[0])
        cli_action_loggers.on_pre_execution(**metrics)
        try:
            return f(*args, **kwargs)
        except Exception as e:
            metrics['error'] = e
            raise
        finally:
            metrics['end_datetime'] = datetime.utcnow()
            cli_action_loggers.on_post_execution(**metrics)
    return wrapper