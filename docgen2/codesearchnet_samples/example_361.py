def xcom_push(self, key, value, execution_date=None):
    if execution_date and execution_date < self.execution_date:
        raise ValueError('execution_date can not be in the past (current execution_date is {}; received {})'.format(self.execution_date, execution_date))
    XCom.set(key=key, value=value, task_id=self.task_id, dag_id=self.dag_id, execution_date=execution_date or self.execution_date)