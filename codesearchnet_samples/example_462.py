def process_result_value(self, value, dialect):
    if value is not None:
        if value.tzinfo is None:
            value = value.replace(tzinfo=utc)
        else:
            value = value.astimezone(utc)
    return value