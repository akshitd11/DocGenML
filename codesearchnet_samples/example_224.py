def remove_option(self, section, option, remove_default=True):
    if super().has_option(section, option):
        super().remove_option(section, option)
    if self.airflow_defaults.has_option(section, option) and remove_default:
        self.airflow_defaults.remove_option(section, option)