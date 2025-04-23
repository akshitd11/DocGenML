def refresh_from_db(self, session=None, lock_for_update=False):
    TI = TaskInstance
    qry = session.query(TI).filter(TI.dag_id == self.dag_id, TI.task_id == self.task_id, TI.execution_date == self.execution_date)
    if lock_for_update:
        ti = qry.with_for_update().first()
    else:
        ti = qry.first()
    if ti:
        self.state = ti.state
        self.start_date = ti.start_date
        self.end_date = ti.end_date
        self.try_number = ti._try_number
        self.max_tries = ti.max_tries
        self.hostname = ti.hostname
        self.pid = ti.pid
        self.executor_config = ti.executor_config
    else:
        self.state = None