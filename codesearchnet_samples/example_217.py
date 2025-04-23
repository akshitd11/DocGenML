def _make_safe_pod_id(safe_dag_id, safe_task_id, safe_uuid):
    MAX_POD_ID_LEN = 253
    safe_key = safe_dag_id + safe_task_id
    safe_pod_id = safe_key[:MAX_POD_ID_LEN - len(safe_uuid) - 1] + '-' + safe_uuid
    return safe_pod_id