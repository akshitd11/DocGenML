def key(self):
    return (self.dag_id, self.task_id, self.execution_date, self.try_number)