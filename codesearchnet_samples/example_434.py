def get_available_fields(self, obj):
    self.get_conn()
    obj_description = self.describe_object(obj)
    return [field['name'] for field in obj_description['fields']]