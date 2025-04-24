def get_instance_template(self, resource_id, project_id=None):
    response = self.get_conn().instanceTemplates().get(project=project_id, instanceTemplate=resource_id).execute(num_retries=self.num_retries)
    return response