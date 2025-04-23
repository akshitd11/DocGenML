def setdefault(cls, key, default, deserialize_json=False):
    obj = Variable.get(key, default_var=None, deserialize_json=deserialize_json)
    if obj is None:
        if default is not None:
            Variable.set(key, default, serialize_json=deserialize_json)
            return default
        else:
            raise ValueError('Default Value must be set')
    else:
        return obj