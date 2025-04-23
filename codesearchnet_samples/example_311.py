def get_task_instances(self, state=None, session=None):
    from airflow.models.taskinstance import TaskInstance
    tis = session.query(TaskInstance).filter(TaskInstance.dag_id == self.dag_id, TaskInstance.execution_date == self.execution_date)
    if state:
        if isinstance(state, six.string_types):
            tis = tis.filter(TaskInstance.state == state)
        elif None in state:
            tis = tis.filter(or_(TaskInstance.state.in_(state), TaskInstance.state.is_(None)))
        else:
            tis = tis.filter(TaskInstance.state.in_(state))
    if self.dag and self.dag.partial:
        tis = tis.filter(TaskInstance.task_id.in_(self.dag.task_ids))
    return tis.all()