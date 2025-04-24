def _to_timestamp(cls, column):
    try:
        column = pd.to_datetime(column)
    except ValueError:
        log = LoggingMixin().log
        log.warning('Could not convert field to timestamps: %s', column.name)
        return column
    converted = []
    for value in column:
        try:
            converted.append(value.timestamp())
        except (ValueError, AttributeError):
            converted.append(pd.np.NaN)
    return pd.Series(converted, index=column.index)