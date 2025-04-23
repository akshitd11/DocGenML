def _get_pretty_exception_message(e):
    if hasattr(e, 'message') and 'errorName' in e.message and ('message' in e.message):
        return '{name}: {message}'.format(name=e.message['errorName'], message=e.message['message'])
    else:
        return str(e)