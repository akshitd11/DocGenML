def clear_xcom_data(self, session=None):
    session.query(XCom).filter(XCom.dag_id == self.dag_id, XCom.task_id == self.task_id, XCom.execution_date == self.execution_date).delete()
    session.commit()