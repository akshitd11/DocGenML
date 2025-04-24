def chain(*tasks):
    for (up_task, down_task) in zip(tasks[:-1], tasks[1:]):
        up_task.set_downstream(down_task)