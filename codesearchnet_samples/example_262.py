def _deep_string_coerce(content, json_path='json'):
    c = _deep_string_coerce
    if isinstance(content, six.string_types):
        return content
    elif isinstance(content, six.integer_types + (float,)):
        return str(content)
    elif isinstance(content, (list, tuple)):
        return [c(e, '{0}[{1}]'.format(json_path, i)) for (i, e) in enumerate(content)]
    elif isinstance(content, dict):
        return {k: c(v, '{0}[{1}]'.format(json_path, k)) for (k, v) in list(content.items())}
    else:
        param_type = type(content)
        msg = 'Type {0} used for parameter {1} is not a number or a string'.format(param_type, json_path)
        raise AirflowException(msg)