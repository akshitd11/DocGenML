def has_task(self, task_instance):
    if task_instance.key in self.queued_tasks or task_instance.key in self.running:
        return True