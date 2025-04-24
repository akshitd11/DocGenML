def pool_full(self, session):
    if not self.task.pool:
        return False
    pool = session.query(Pool).filter(Pool.pool == self.task.pool).first()
    if not pool:
        return False
    open_slots = pool.open_slots(session=session)
    return open_slots <= 0