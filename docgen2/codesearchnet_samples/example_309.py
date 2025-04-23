def refresh_from_db(self, session=None):
    DR = DagRun
    exec_date = func.cast(self.execution_date, DateTime)
    dr = session.query(DR).filter(DR.dag_id == self.dag_id, func.cast(DR.execution_date, DateTime) == exec_date, DR.run_id == self.run_id).one()
    self.id = dr.id
    self.state = dr.state