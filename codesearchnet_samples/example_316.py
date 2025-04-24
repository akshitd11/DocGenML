def verify_integrity(self, session=None):
    from airflow.models.taskinstance import TaskInstance
    dag = self.get_dag()
    tis = self.get_task_instances(session=session)
    task_ids = []
    for ti in tis:
        task_ids.append(ti.task_id)
        task = None
        try:
            task = dag.get_task(ti.task_id)
        except AirflowException:
            if ti.state == State.REMOVED:
                pass
            elif self.state is not State.RUNNING and (not dag.partial):
                self.log.warning("Failed to get task '{}' for dag '{}'. Marking it as removed.".format(ti, dag))
                Stats.incr('task_removed_from_dag.{}'.format(dag.dag_id), 1, 1)
                ti.state = State.REMOVED
        is_task_in_dag = task is not None
        should_restore_task = is_task_in_dag and ti.state == State.REMOVED
        if should_restore_task:
            self.log.info("Restoring task '{}' which was previously removed from DAG '{}'".format(ti, dag))
            Stats.incr('task_restored_to_dag.{}'.format(dag.dag_id), 1, 1)
            ti.state = State.NONE
    for task in six.itervalues(dag.task_dict):
        if task.start_date > self.execution_date and (not self.is_backfill):
            continue
        if task.task_id not in task_ids:
            Stats.incr('task_instance_created-{}'.format(task.__class__.__name__), 1, 1)
            ti = TaskInstance(task, self.execution_date)
            session.add(ti)
    session.commit()