def process_file(self, filepath, only_if_updated=True, safe_mode=True):
    from airflow.models.dag import DAG
    found_dags = []
    if filepath is None or not os.path.isfile(filepath):
        return found_dags
    try:
        file_last_changed_on_disk = datetime.fromtimestamp(os.path.getmtime(filepath))
        if only_if_updated and filepath in self.file_last_changed and (file_last_changed_on_disk == self.file_last_changed[filepath]):
            return found_dags
    except Exception as e:
        self.log.exception(e)
        return found_dags
    mods = []
    is_zipfile = zipfile.is_zipfile(filepath)
    if not is_zipfile:
        if safe_mode:
            with open(filepath, 'rb') as f:
                content = f.read()
                if not all([s in content for s in (b'DAG', b'airflow')]):
                    self.file_last_changed[filepath] = file_last_changed_on_disk
                    if not self.has_logged:
                        self.has_logged = True
                        self.log.info('File %s assumed to contain no DAGs. Skipping.', filepath)
                    return found_dags
        self.log.debug('Importing %s', filepath)
        (org_mod_name, _) = os.path.splitext(os.path.split(filepath)[-1])
        mod_name = 'unusual_prefix_' + hashlib.sha1(filepath.encode('utf-8')).hexdigest() + '_' + org_mod_name
        if mod_name in sys.modules:
            del sys.modules[mod_name]
        with timeout(configuration.conf.getint('core', 'DAGBAG_IMPORT_TIMEOUT')):
            try:
                m = imp.load_source(mod_name, filepath)
                mods.append(m)
            except Exception as e:
                self.log.exception('Failed to import: %s', filepath)
                self.import_errors[filepath] = str(e)
                self.file_last_changed[filepath] = file_last_changed_on_disk
    else:
        zip_file = zipfile.ZipFile(filepath)
        for mod in zip_file.infolist():
            (head, _) = os.path.split(mod.filename)
            (mod_name, ext) = os.path.splitext(mod.filename)
            if not head and (ext == '.py' or ext == '.pyc'):
                if mod_name == '__init__':
                    self.log.warning('Found __init__.%s at root of %s', ext, filepath)
                if safe_mode:
                    with zip_file.open(mod.filename) as zf:
                        self.log.debug('Reading %s from %s', mod.filename, filepath)
                        content = zf.read()
                        if not all([s in content for s in (b'DAG', b'airflow')]):
                            self.file_last_changed[filepath] = file_last_changed_on_disk
                            if not self.has_logged:
                                self.has_logged = True
                                self.log.info('File %s assumed to contain no DAGs. Skipping.', filepath)
                if mod_name in sys.modules:
                    del sys.modules[mod_name]
                try:
                    sys.path.insert(0, filepath)
                    m = importlib.import_module(mod_name)
                    mods.append(m)
                except Exception as e:
                    self.log.exception('Failed to import: %s', filepath)
                    self.import_errors[filepath] = str(e)
                    self.file_last_changed[filepath] = file_last_changed_on_disk
    for m in mods:
        for dag in list(m.__dict__.values()):
            if isinstance(dag, DAG):
                if not dag.full_filepath:
                    dag.full_filepath = filepath
                    if dag.fileloc != filepath and (not is_zipfile):
                        dag.fileloc = filepath
                try:
                    dag.is_subdag = False
                    self.bag_dag(dag, parent_dag=dag, root_dag=dag)
                    if isinstance(dag._schedule_interval, six.string_types):
                        croniter(dag._schedule_interval)
                    found_dags.append(dag)
                    found_dags += dag.subdags
                except (CroniterBadCronError, CroniterBadDateError, CroniterNotAlphaError) as cron_e:
                    self.log.exception('Failed to bag_dag: %s', dag.full_filepath)
                    self.import_errors[dag.full_filepath] = 'Invalid Cron expression: ' + str(cron_e)
                    self.file_last_changed[dag.full_filepath] = file_last_changed_on_disk
                except AirflowDagCycleException as cycle_exception:
                    self.log.exception('Failed to bag_dag: %s', dag.full_filepath)
                    self.import_errors[dag.full_filepath] = str(cycle_exception)
                    self.file_last_changed[dag.full_filepath] = file_last_changed_on_disk
    self.file_last_changed[filepath] = file_last_changed_on_disk
    return found_dags