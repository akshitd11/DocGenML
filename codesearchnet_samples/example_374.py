def get_instance_group_manager(self, zone, resource_id, project_id=None):
    response = self.get_conn().instanceGroupManagers().get(project=project_id, zone=zone, instanceGroupManager=resource_id).execute(num_retries=self.num_retries)
    return response