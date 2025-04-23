def _convert_to_float_if_possible(s):
    try:
        ret = float(s)
    except (ValueError, TypeError):
        ret = s
    return ret