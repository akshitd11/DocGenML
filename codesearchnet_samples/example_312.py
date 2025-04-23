def get_task_instance(self, task_id, session=None):
    from airflow.models.taskinstance import TaskInstance
    TI = TaskInstance
    ti = session.query(TI).filter(TI.dag_id == self.dag_id, TI.execution_date == self.execution_date, TI.task_id == task_id).first()
    return ti