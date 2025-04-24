def current_state(self, session=None):
    TI = TaskInstance
    ti = session.query(TI).filter(TI.dag_id == self.dag_id, TI.task_id == self.task_id, TI.execution_date == self.execution_date).all()
    if ti:
        state = ti[0].state
    else:
        state = None
    return state