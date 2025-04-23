def convert_tuple_type(cls, name, value):
    names = ['field_' + str(i) for i in range(len(value))]
    values = [cls.convert_value(name, value) for (name, value) in zip(names, value)]
    return cls.generate_data_dict(names, values)