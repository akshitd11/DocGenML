def list_py_file_paths(directory, safe_mode=True, include_examples=None):
    if include_examples is None:
        include_examples = conf.getboolean('core', 'LOAD_EXAMPLES')
    file_paths = []
    if directory is None:
        return []
    elif os.path.isfile(directory):
        return [directory]
    elif os.path.isdir(directory):
        patterns_by_dir = {}
        for (root, dirs, files) in os.walk(directory, followlinks=True):
            patterns = patterns_by_dir.get(root, [])
            ignore_file = os.path.join(root, '.airflowignore')
            if os.path.isfile(ignore_file):
                with open(ignore_file, 'r') as f:
                    patterns += [re.compile(p) for p in f.read().split('\n') if p]
            dirs[:] = [d for d in dirs if not any((p.search(os.path.join(root, d)) for p in patterns))]
            for d in dirs:
                patterns_by_dir[os.path.join(root, d)] = patterns
            for f in files:
                try:
                    file_path = os.path.join(root, f)
                    if not os.path.isfile(file_path):
                        continue
                    (mod_name, file_ext) = os.path.splitext(os.path.split(file_path)[-1])
                    if file_ext != '.py' and (not zipfile.is_zipfile(file_path)):
                        continue
                    if any([re.findall(p, file_path) for p in patterns]):
                        continue
                    might_contain_dag = True
                    if safe_mode and (not zipfile.is_zipfile(file_path)):
                        with open(file_path, 'rb') as fp:
                            content = fp.read()
                            might_contain_dag = all([s in content for s in (b'DAG', b'airflow')])
                    if not might_contain_dag:
                        continue
                    file_paths.append(file_path)
                except Exception:
                    log = LoggingMixin().log
                    log.exception('Error while examining %s', f)
    if include_examples:
        import airflow.example_dags
        example_dag_folder = airflow.example_dags.__path__[0]
        file_paths.extend(list_py_file_paths(example_dag_folder, safe_mode, False))
    return file_paths