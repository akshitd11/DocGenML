def bag_dag(self, dag, parent_dag, root_dag):
    dag.test_cycle()
    dag.resolve_template_files()
    dag.last_loaded = timezone.utcnow()
    for task in dag.tasks:
        settings.policy(task)
    subdags = dag.subdags
    try:
        for subdag in subdags:
            subdag.full_filepath = dag.full_filepath
            subdag.parent_dag = dag
            subdag.is_subdag = True
            self.bag_dag(subdag, parent_dag=dag, root_dag=root_dag)
        self.dags[dag.dag_id] = dag
        self.log.debug('Loaded DAG %s', dag)
    except AirflowDagCycleException as cycle_exception:
        self.log.exception('Exception bagging dag: %s', dag.dag_id)
        if dag == root_dag:
            for subdag in subdags:
                if subdag.dag_id in self.dags:
                    del self.dags[subdag.dag_id]
        raise cycle_exception