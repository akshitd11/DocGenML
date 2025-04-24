def _build_metrics(func_name, namespace):
    metrics = {'sub_command': func_name, 'start_datetime': datetime.utcnow(), 'full_command': '{}'.format(list(sys.argv)), 'user': getpass.getuser()}
    assert isinstance(namespace, Namespace)
    tmp_dic = vars(namespace)
    metrics['dag_id'] = tmp_dic.get('dag_id')
    metrics['task_id'] = tmp_dic.get('task_id')
    metrics['execution_date'] = tmp_dic.get('execution_date')
    metrics['host_name'] = socket.gethostname()
    extra = json.dumps(dict(((k, metrics[k]) for k in ('host_name', 'full_command'))))
    log = Log(event='cli_{}'.format(func_name), task_instance=None, owner=metrics['user'], extra=extra, task_id=metrics.get('task_id'), dag_id=metrics.get('dag_id'), execution_date=metrics.get('execution_date'))
    metrics['log'] = log
    return metrics