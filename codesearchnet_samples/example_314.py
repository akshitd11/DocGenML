def get_previous_scheduled_dagrun(self, session=None):
    dag = self.get_dag()
    return session.query(DagRun).filter(DagRun.dag_id == self.dag_id, DagRun.execution_date == dag.previous_schedule(self.execution_date)).first()