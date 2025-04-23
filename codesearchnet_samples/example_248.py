def prepare_classpath():
    if DAGS_FOLDER not in sys.path:
        sys.path.append(DAGS_FOLDER)
    config_path = os.path.join(AIRFLOW_HOME, 'config')
    if config_path not in sys.path:
        sys.path.append(config_path)
    if PLUGINS_FOLDER not in sys.path:
        sys.path.append(PLUGINS_FOLDER)