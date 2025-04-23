def get_dagrun(self, session):
    from airflow.models.dagrun import DagRun
    dr = session.query(DagRun).filter(DagRun.dag_id == self.dag_id, DagRun.execution_date == self.execution_date).first()
    return dr