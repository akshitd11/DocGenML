def get_instance(self, instance, project_id=None):
    return self.get_conn().instances().get(project=project_id, instance=instance).execute(num_retries=self.num_retries)