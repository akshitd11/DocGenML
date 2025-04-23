def _closest_date(target_dt, date_list, before_target=None):
    fb = lambda d: target_dt - d if d <= target_dt else datetime.timedelta.max
    fa = lambda d: d - target_dt if d >= target_dt else datetime.timedelta.max
    fnone = lambda d: target_dt - d if d < target_dt else d - target_dt
    if before_target is None:
        return min(date_list, key=fnone).date()
    if before_target:
        return min(date_list, key=fb).date()
    else:
        return min(date_list, key=fa).date()