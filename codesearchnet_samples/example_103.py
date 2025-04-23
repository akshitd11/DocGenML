def _integrate_plugins():
    import sys
    from airflow.plugins_manager import sensors_modules
    for sensors_module in sensors_modules:
        sys.modules[sensors_module.__name__] = sensors_module
        globals()[sensors_module._name] = sensors_module