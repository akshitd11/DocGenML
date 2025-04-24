def task_failed_deps(args):
    dag = get_dag(args)
    task = dag.get_task(task_id=args.task_id)
    ti = TaskInstance(task, args.execution_date)
    dep_context = DepContext(deps=SCHEDULER_DEPS)
    failed_deps = list(ti.get_failed_dep_statuses(dep_context=dep_context))
    if failed_deps:
        print('Task instance dependencies not met:')
        for dep in failed_deps:
            print('{}: {}'.format(dep.dep_name, dep.reason))
    else:
        print('Task instance dependencies are all met.')