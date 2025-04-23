def convert_to_utc(value):
    if not value:
        return value
    if not is_localized(value):
        value = pendulum.instance(value, TIMEZONE)
    return value.astimezone(utc)