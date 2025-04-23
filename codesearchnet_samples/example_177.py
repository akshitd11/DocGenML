def get_dag(self, dag_id):
    if dag_id not in self.dag_id_to_simple_dag:
        raise AirflowException('Unknown DAG ID {}'.format(dag_id))
    return self.dag_id_to_simple_dag[dag_id]