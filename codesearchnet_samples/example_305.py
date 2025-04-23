def apply_defaults(func):
    sig_cache = signature(func)
    non_optional_args = {name for (name, param) in sig_cache.parameters.items() if param.default == param.empty and param.name != 'self' and (param.kind not in (param.VAR_POSITIONAL, param.VAR_KEYWORD))}

    @wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) > 1:
            raise AirflowException('Use keyword arguments when initializing operators')
        dag_args = {}
        dag_params = {}
        dag = kwargs.get('dag', None) or settings.CONTEXT_MANAGER_DAG
        if dag:
            dag_args = copy(dag.default_args) or {}
            dag_params = copy(dag.params) or {}
        params = {}
        if 'params' in kwargs:
            params = kwargs['params']
        dag_params.update(params)
        default_args = {}
        if 'default_args' in kwargs:
            default_args = kwargs['default_args']
            if 'params' in default_args:
                dag_params.update(default_args['params'])
                del default_args['params']
        dag_args.update(default_args)
        default_args = dag_args
        for arg in sig_cache.parameters:
            if arg not in kwargs and arg in default_args:
                kwargs[arg] = default_args[arg]
        missing_args = list(non_optional_args - set(kwargs))
        if missing_args:
            msg = 'Argument {0} is required'.format(missing_args)
            raise AirflowException(msg)
        kwargs['params'] = dag_params
        result = func(*args, **kwargs)
        return result
    return wrapper