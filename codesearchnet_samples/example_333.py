def kill_zombies(self, zombies, session=None):
    from airflow.models.taskinstance import TaskInstance
    for zombie in zombies:
        if zombie.dag_id in self.dags:
            dag = self.dags[zombie.dag_id]
            if zombie.task_id in dag.task_ids:
                task = dag.get_task(zombie.task_id)
                ti = TaskInstance(task, zombie.execution_date)
                ti.start_date = zombie.start_date
                ti.end_date = zombie.end_date
                ti.try_number = zombie.try_number
                ti.state = zombie.state
                ti.test_mode = configuration.getboolean('core', 'unit_test_mode')
                ti.handle_failure('{} detected as zombie'.format(ti), ti.test_mode, ti.get_template_context())
                self.log.info('Marked zombie job %s as %s', ti, ti.state)
                Stats.incr('zombies_killed')
    session.commit()