def _get_field(self, extras, field, default=None):
    long_f = 'extra__google_cloud_platform__{}'.format(field)
    if long_f in extras:
        return extras[long_f]
    else:
        self.log.info('Field %s not found in extras.', field)
        return default