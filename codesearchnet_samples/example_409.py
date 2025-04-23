def is_valid_plugin(plugin_obj, existing_plugins):
    if inspect.isclass(plugin_obj) and issubclass(plugin_obj, AirflowPlugin) and (plugin_obj is not AirflowPlugin):
        plugin_obj.validate()
        return plugin_obj not in existing_plugins
    return False