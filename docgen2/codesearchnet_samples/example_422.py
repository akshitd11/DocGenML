def convert_types(cls, value):
    if isinstance(value, decimal.Decimal):
        return float(value)
    else:
        return value