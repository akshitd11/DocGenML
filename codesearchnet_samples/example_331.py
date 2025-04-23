def get_dag(self, dag_id):
    from airflow.models.dag import DagModel
    root_dag_id = dag_id
    if dag_id in self.dags:
        dag = self.dags[dag_id]
        if dag.is_subdag:
            root_dag_id = dag.parent_dag.dag_id
    orm_dag = DagModel.get_current(root_dag_id)
    if orm_dag and (root_dag_id not in self.dags or (orm_dag.last_expired and dag.last_loaded < orm_dag.last_expired)):
        found_dags = self.process_file(filepath=orm_dag.fileloc, only_if_updated=False)
        if found_dags and dag_id in [found_dag.dag_id for found_dag in found_dags]:
            return self.dags[dag_id]
        elif dag_id in self.dags:
            del self.dags[dag_id]
    return self.dags.get(dag_id)