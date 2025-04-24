def is_met(self, ti, session, dep_context=None):
    return all((status.passed for status in self.get_dep_statuses(ti, session, dep_context)))