def are_dependencies_met(self, dep_context=None, session=None, verbose=False):
    dep_context = dep_context or DepContext()
    failed = False
    verbose_aware_logger = self.log.info if verbose else self.log.debug
    for dep_status in self.get_failed_dep_statuses(dep_context=dep_context, session=session):
        failed = True
        verbose_aware_logger("Dependencies not met for %s, dependency '%s' FAILED: %s", self, dep_status.dep_name, dep_status.reason)
    if failed:
        return False
    verbose_aware_logger('Dependencies all met for %s', self)
    return True