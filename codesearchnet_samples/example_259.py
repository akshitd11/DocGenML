def _integrate_plugins():
    import sys
    from airflow.plugins_manager import operators_modules
    for operators_module in operators_modules:
        sys.modules[operators_module.__name__] = operators_module
        globals()[operators_module._name] = operators_module