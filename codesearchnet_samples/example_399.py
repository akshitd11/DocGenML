def convert_map_type(cls, name, value):
    converted_map = []
    for (k, v) in zip(value.keys(), value.values()):
        converted_map.append({'key': cls.convert_value('key', k), 'value': cls.convert_value('value', v)})
    return converted_map