def conditionally_trigger(context, dag_run_obj):
    c_p = context['params']['condition_param']
    print('Controller DAG : conditionally_trigger = {}'.format(c_p))
    if context['params']['condition_param']:
        dag_run_obj.payload = {'message': context['params']['message']}
        pp.pprint(dag_run_obj.payload)
        return dag_run_obj