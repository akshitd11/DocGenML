def exists(self, resource_group, name):
    for container in self.connection.container_groups.list_by_resource_group(resource_group):
        if container.name == name:
            return True
    return False