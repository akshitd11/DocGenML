def are_dependents_done(self, session=None):
    task = self.task
    if not task.downstream_task_ids:
        return True
    ti = session.query(func.count(TaskInstance.task_id)).filter(TaskInstance.dag_id == self.dag_id, TaskInstance.task_id.in_(task.downstream_task_ids), TaskInstance.execution_date == self.execution_date, TaskInstance.state == State.SUCCESS)
    count = ti[0][0]
    return count == len(task.downstream_task_ids)