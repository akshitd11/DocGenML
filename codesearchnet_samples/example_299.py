def create_or_update(self, resource_group, name, container_group):
    self.connection.container_groups.create_or_update(resource_group, name, container_group)