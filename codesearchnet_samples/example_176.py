def construct_task_instance(self, session=None, lock_for_update=False):
    TI = airflow.models.TaskInstance
    qry = session.query(TI).filter(TI.dag_id == self._dag_id, TI.task_id == self._task_id, TI.execution_date == self._execution_date)
    if lock_for_update:
        ti = qry.with_for_update().first()
    else:
        ti = qry.first()
    return ti