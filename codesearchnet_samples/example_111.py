def create_evaluate_ops(task_prefix, data_format, input_paths, prediction_path, metric_fn_and_keys, validate_fn, batch_prediction_job_id=None, project_id=None, region=None, dataflow_options=None, model_uri=None, model_name=None, version_name=None, dag=None):
    if not re.match('^[a-zA-Z][-A-Za-z0-9]*$', task_prefix):
        raise AirflowException('Malformed task_id for DataFlowPythonOperator (only alphanumeric and hyphens are allowed but got: ' + task_prefix)
    (metric_fn, metric_keys) = metric_fn_and_keys
    if not callable(metric_fn):
        raise AirflowException('`metric_fn` param must be callable.')
    if not callable(validate_fn):
        raise AirflowException('`validate_fn` param must be callable.')
    if dag is not None and dag.default_args is not None:
        default_args = dag.default_args
        project_id = project_id or default_args.get('project_id')
        region = region or default_args.get('region')
        model_name = model_name or default_args.get('model_name')
        version_name = version_name or default_args.get('version_name')
        dataflow_options = dataflow_options or default_args.get('dataflow_default_options')
    evaluate_prediction = MLEngineBatchPredictionOperator(task_id=task_prefix + '-prediction', project_id=project_id, job_id=batch_prediction_job_id, region=region, data_format=data_format, input_paths=input_paths, output_path=prediction_path, uri=model_uri, model_name=model_name, version_name=version_name, dag=dag)
    metric_fn_encoded = base64.b64encode(dill.dumps(metric_fn, recurse=True))
    evaluate_summary = DataFlowPythonOperator(task_id=task_prefix + '-summary', py_options=['-m'], py_file='airflow.contrib.utils.mlengine_prediction_summary', dataflow_default_options=dataflow_options, options={'prediction_path': prediction_path, 'metric_fn_encoded': metric_fn_encoded, 'metric_keys': ','.join(metric_keys)}, dag=dag)
    evaluate_summary.set_upstream(evaluate_prediction)

    def apply_validate_fn(*args, **kwargs):
        prediction_path = kwargs['templates_dict']['prediction_path']
        (scheme, bucket, obj, _, _) = urlsplit(prediction_path)
        if scheme != 'gs' or not bucket or (not obj):
            raise ValueError('Wrong format prediction_path: %s', prediction_path)
        summary = os.path.join(obj.strip('/'), 'prediction.summary.json')
        gcs_hook = GoogleCloudStorageHook()
        summary = json.loads(gcs_hook.download(bucket, summary))
        return validate_fn(summary)
    evaluate_validation = PythonOperator(task_id=task_prefix + '-validation', python_callable=apply_validate_fn, provide_context=True, templates_dict={'prediction_path': prediction_path}, dag=dag)
    evaluate_validation.set_upstream(evaluate_summary)
    return (evaluate_prediction, evaluate_summary, evaluate_validation)