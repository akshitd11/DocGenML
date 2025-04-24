def get_hostname():
    try:
        callable_path = conf.get('core', 'hostname_callable')
    except AirflowConfigException:
        callable_path = None
    if not callable_path:
        return socket.getfqdn()
    (module_path, attr_name) = callable_path.split(':')
    module = importlib.import_module(module_path)
    callable = getattr(module, attr_name)
    return callable()