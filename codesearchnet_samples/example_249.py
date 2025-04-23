def _check_task_id(self, context):
    ti = context['ti']
    celery_result = ti.xcom_pull(task_ids=self.target_task_id)
    return celery_result.ready()