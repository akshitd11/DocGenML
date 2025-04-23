def task_state(args):
    dag = get_dag(args)
    task = dag.get_task(task_id=args.task_id)
    ti = TaskInstance(task, args.execution_date)
    print(ti.current_state())