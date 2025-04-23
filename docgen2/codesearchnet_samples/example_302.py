def get_logs(self, resource_group, name, tail=1000):
    logs = self.connection.container.list_logs(resource_group, name, name, tail=tail)
    return logs.content.splitlines(True)