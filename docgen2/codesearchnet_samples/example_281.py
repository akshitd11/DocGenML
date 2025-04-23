def _integrate_plugins():
    from airflow.plugins_manager import executors_modules
    for executors_module in executors_modules:
        sys.modules[executors_module.__name__] = executors_module
        globals()[executors_module._name] = executors_module