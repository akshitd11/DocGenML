def open_slots(self, session):
    from airflow.models.taskinstance import TaskInstance as TI
    used_slots = session.query(func.count()).filter(TI.pool == self.pool).filter(TI.state.in_([State.RUNNING, State.QUEUED])).scalar()
    return self.slots - used_slots