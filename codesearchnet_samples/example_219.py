def clear_not_launched_queued_tasks(self, session=None):
    queued_tasks = session.query(TaskInstance).filter(TaskInstance.state == State.QUEUED).all()
    self.log.info('When executor started up, found %s queued task instances', len(queued_tasks))
    for task in queued_tasks:
        dict_string = 'dag_id={},task_id={},execution_date={},airflow-worker={}'.format(AirflowKubernetesScheduler._make_safe_label_value(task.dag_id), AirflowKubernetesScheduler._make_safe_label_value(task.task_id), AirflowKubernetesScheduler._datetime_to_label_safe_datestring(task.execution_date), self.worker_uuid)
        kwargs = dict(label_selector=dict_string)
        pod_list = self.kube_client.list_namespaced_pod(self.kube_config.kube_namespace, **kwargs)
        if len(pod_list.items) == 0:
            self.log.info('TaskInstance: %s found in queued state but was not launched, rescheduling', task)
            session.query(TaskInstance).filter(TaskInstance.dag_id == task.dag_id, TaskInstance.task_id == task.task_id, TaskInstance.execution_date == task.execution_date).update({TaskInstance.state: State.NONE})