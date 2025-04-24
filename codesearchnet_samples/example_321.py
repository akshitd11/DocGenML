def context_to_airflow_vars(context, in_env_var_format=False):
    params = dict()
    if in_env_var_format:
        name_format = 'env_var_format'
    else:
        name_format = 'default'
    task_instance = context.get('task_instance')
    if task_instance and task_instance.dag_id:
        params[AIRFLOW_VAR_NAME_FORMAT_MAPPING['AIRFLOW_CONTEXT_DAG_ID'][name_format]] = task_instance.dag_id
    if task_instance and task_instance.task_id:
        params[AIRFLOW_VAR_NAME_FORMAT_MAPPING['AIRFLOW_CONTEXT_TASK_ID'][name_format]] = task_instance.task_id
    if task_instance and task_instance.execution_date:
        params[AIRFLOW_VAR_NAME_FORMAT_MAPPING['AIRFLOW_CONTEXT_EXECUTION_DATE'][name_format]] = task_instance.execution_date.isoformat()
    dag_run = context.get('dag_run')
    if dag_run and dag_run.run_id:
        params[AIRFLOW_VAR_NAME_FORMAT_MAPPING['AIRFLOW_CONTEXT_DAG_RUN_ID'][name_format]] = dag_run.run_id
    return params