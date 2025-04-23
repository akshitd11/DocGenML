def as_dict(self, display_source=False, display_sensitive=False, raw=False):
    cfg = {}
    configs = [('default', self.airflow_defaults), ('airflow.cfg', self)]
    for (source_name, config) in configs:
        for section in config.sections():
            sect = cfg.setdefault(section, OrderedDict())
            for (k, val) in config.items(section=section, raw=raw):
                if display_source:
                    val = (val, source_name)
                sect[k] = val
    for ev in [ev for ev in os.environ if ev.startswith('AIRFLOW__')]:
        try:
            (_, section, key) = ev.split('__')
            opt = self._get_env_var_option(section, key)
        except ValueError:
            continue
        if not display_sensitive and ev != 'AIRFLOW__CORE__UNIT_TEST_MODE':
            opt = '< hidden >'
        elif raw:
            opt = opt.replace('%', '%%')
        if display_source:
            opt = (opt, 'env var')
        cfg.setdefault(section.lower(), OrderedDict()).update({key.lower(): opt})
    for (section, key) in self.as_command_stdout:
        opt = self._get_cmd_option(section, key)
        if opt:
            if not display_sensitive:
                opt = '< hidden >'
            if display_source:
                opt = (opt, 'cmd')
            elif raw:
                opt = opt.replace('%', '%%')
            cfg.setdefault(section, OrderedDict()).update({key: opt})
            del cfg[section][key + '_cmd']
    return cfg