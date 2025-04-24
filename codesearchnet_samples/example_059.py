def _get_field(self, field_name, default=None):
    full_field_name = 'extra__grpc__{}'.format(field_name)
    if full_field_name in self.extras:
        return self.extras[full_field_name]
    else:
        return default