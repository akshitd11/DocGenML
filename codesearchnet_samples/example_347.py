def generate_command(dag_id, task_id, execution_date, mark_success=False, ignore_all_deps=False, ignore_depends_on_past=False, ignore_task_deps=False, ignore_ti_state=False, local=False, pickle_id=None, file_path=None, raw=False, job_id=None, pool=None, cfg_path=None):
    iso = execution_date.isoformat()
    cmd = ['airflow', 'run', str(dag_id), str(task_id), str(iso)]
    cmd.extend(['--mark_success']) if mark_success else None
    cmd.extend(['--pickle', str(pickle_id)]) if pickle_id else None
    cmd.extend(['--job_id', str(job_id)]) if job_id else None
    cmd.extend(['-A']) if ignore_all_deps else None
    cmd.extend(['-i']) if ignore_task_deps else None
    cmd.extend(['-I']) if ignore_depends_on_past else None
    cmd.extend(['--force']) if ignore_ti_state else None
    cmd.extend(['--local']) if local else None
    cmd.extend(['--pool', pool]) if pool else None
    cmd.extend(['--raw']) if raw else None
    cmd.extend(['-sd', file_path]) if file_path else None
    cmd.extend(['--cfg_path', cfg_path]) if cfg_path else None
    return cmd