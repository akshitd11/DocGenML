def delete(self, resource_group, name):
    self.connection.container_groups.delete(resource_group, name)