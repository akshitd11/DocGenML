def get_dep_statuses(self, ti, session, dep_context=None):
    from airflow.ti_deps.dep_context import DepContext
    if dep_context is None:
        dep_context = DepContext()
    if self.IGNOREABLE and dep_context.ignore_all_deps:
        yield self._passing_status(reason='Context specified all dependencies should be ignored.')
        return
    if self.IS_TASK_DEP and dep_context.ignore_task_deps:
        yield self._passing_status(reason='Context specified all task dependencies should be ignored.')
        return
    for dep_status in self._get_dep_statuses(ti, session, dep_context):
        yield dep_status