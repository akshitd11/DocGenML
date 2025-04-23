def alchemy_to_dict(obj):
    if not obj:
        return None
    d = {}
    for c in obj.__table__.columns:
        value = getattr(obj, c.name)
        if type(value) == datetime:
            value = value.isoformat()
        d[c.name] = value
    return d