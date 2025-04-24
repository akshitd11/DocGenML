def xcom_pull(self, task_ids=None, dag_id=None, key=XCOM_RETURN_KEY, include_prior_dates=False):
    if dag_id is None:
        dag_id = self.dag_id
    pull_fn = functools.partial(XCom.get_one, execution_date=self.execution_date, key=key, dag_id=dag_id, include_prior_dates=include_prior_dates)
    if is_container(task_ids):
        return tuple((pull_fn(task_id=t) for t in task_ids))
    else:
        return pull_fn(task_id=task_ids)