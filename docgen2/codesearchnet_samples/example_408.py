def load_entrypoint_plugins(entry_points, airflow_plugins):
    for entry_point in entry_points:
        log.debug('Importing entry_point plugin %s', entry_point.name)
        plugin_obj = entry_point.load()
        if is_valid_plugin(plugin_obj, airflow_plugins):
            if callable(getattr(plugin_obj, 'on_load', None)):
                plugin_obj.on_load()
                airflow_plugins.append(plugin_obj)
    return airflow_plugins