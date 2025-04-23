def collect_dags(self, dag_folder=None, only_if_updated=True, include_examples=configuration.conf.getboolean('core', 'LOAD_EXAMPLES'), safe_mode=configuration.conf.getboolean('core', 'DAG_DISCOVERY_SAFE_MODE')):
    start_dttm = timezone.utcnow()
    dag_folder = dag_folder or self.dag_folder
    stats = []
    FileLoadStat = namedtuple('FileLoadStat', 'file duration dag_num task_num dags')
    dag_folder = correct_maybe_zipped(dag_folder)
    for filepath in list_py_file_paths(dag_folder, safe_mode=safe_mode, include_examples=include_examples):
        try:
            ts = timezone.utcnow()
            found_dags = self.process_file(filepath, only_if_updated=only_if_updated, safe_mode=safe_mode)
            td = timezone.utcnow() - ts
            td = td.total_seconds() + float(td.microseconds) / 1000000
            stats.append(FileLoadStat(filepath.replace(dag_folder, ''), td, len(found_dags), sum([len(dag.tasks) for dag in found_dags]), str([dag.dag_id for dag in found_dags])))
        except Exception as e:
            self.log.exception(e)
    Stats.gauge('collect_dags', (timezone.utcnow() - start_dttm).total_seconds(), 1)
    Stats.gauge('dagbag_size', len(self.dags), 1)
    Stats.gauge('dagbag_import_errors', len(self.import_errors), 1)
    self.dagbag_stats = sorted(stats, key=lambda x: x.duration, reverse=True)