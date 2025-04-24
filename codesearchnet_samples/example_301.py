def get_messages(self, resource_group, name):
    instance_view = self._get_instance_view(resource_group, name)
    return [event.message for event in instance_view.events]