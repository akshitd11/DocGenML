def make_naive(value, timezone=None):
    if timezone is None:
        timezone = TIMEZONE
    if is_naive(value):
        raise ValueError('make_naive() cannot be applied to a naive datetime')
    o = value.astimezone(timezone)
    naive = dt.datetime(o.year, o.month, o.day, o.hour, o.minute, o.second, o.microsecond)
    return naive