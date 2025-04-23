def _get_executor(executor_name):
    if executor_name == Executors.LocalExecutor:
        return LocalExecutor()
    elif executor_name == Executors.SequentialExecutor:
        return SequentialExecutor()
    elif executor_name == Executors.CeleryExecutor:
        from airflow.executors.celery_executor import CeleryExecutor
        return CeleryExecutor()
    elif executor_name == Executors.DaskExecutor:
        from airflow.executors.dask_executor import DaskExecutor
        return DaskExecutor()
    elif executor_name == Executors.KubernetesExecutor:
        from airflow.contrib.executors.kubernetes_executor import KubernetesExecutor
        return KubernetesExecutor()
    else:
        _integrate_plugins()
        executor_path = executor_name.split('.')
        if len(executor_path) != 2:
            raise AirflowException('Executor {0} not supported: please specify in format plugin_module.executor'.format(executor_name))
        if executor_path[0] in globals():
            return globals()[executor_path[0]].__dict__[executor_path[1]]()
        else:
            raise AirflowException('Executor {0} not supported.'.format(executor_name))