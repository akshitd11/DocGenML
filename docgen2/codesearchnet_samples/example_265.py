def fetch_celery_task_state(celery_task):
    try:
        with timeout(seconds=2):
            res = (celery_task[0], celery_task[1].state)
    except Exception as e:
        exception_traceback = 'Celery Task ID: {}\n{}'.format(celery_task[0], traceback.format_exc())
        res = ExceptionWithTraceback(e, exception_traceback)
    return res