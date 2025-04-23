def _evaluate_trigger_rule(self, ti, successes, skipped, failed, upstream_failed, done, flag_upstream_failed, session):
    TR = airflow.utils.trigger_rule.TriggerRule
    task = ti.task
    upstream = len(task.upstream_task_ids)
    tr = task.trigger_rule
    upstream_done = done >= upstream
    upstream_tasks_state = {'total': upstream, 'successes': successes, 'skipped': skipped, 'failed': failed, 'upstream_failed': upstream_failed, 'done': done}
    if flag_upstream_failed:
        if tr == TR.ALL_SUCCESS:
            if upstream_failed or failed:
                ti.set_state(State.UPSTREAM_FAILED, session)
            elif skipped:
                ti.set_state(State.SKIPPED, session)
        elif tr == TR.ALL_FAILED:
            if successes or skipped:
                ti.set_state(State.SKIPPED, session)
        elif tr == TR.ONE_SUCCESS:
            if upstream_done and (not successes):
                ti.set_state(State.SKIPPED, session)
        elif tr == TR.ONE_FAILED:
            if upstream_done and (not (failed or upstream_failed)):
                ti.set_state(State.SKIPPED, session)
        elif tr == TR.NONE_FAILED:
            if upstream_failed or failed:
                ti.set_state(State.UPSTREAM_FAILED, session)
            elif skipped == upstream:
                ti.set_state(State.SKIPPED, session)
        elif tr == TR.NONE_SKIPPED:
            if skipped:
                ti.set_state(State.SKIPPED, session)
    if tr == TR.ONE_SUCCESS:
        if successes <= 0:
            yield self._failing_status(reason="Task's trigger rule '{0}' requires one upstream task success, but none were found. upstream_tasks_state={1}, upstream_task_ids={2}".format(tr, upstream_tasks_state, task.upstream_task_ids))
    elif tr == TR.ONE_FAILED:
        if not failed and (not upstream_failed):
            yield self._failing_status(reason="Task's trigger rule '{0}' requires one upstream task failure, but none were found. upstream_tasks_state={1}, upstream_task_ids={2}".format(tr, upstream_tasks_state, task.upstream_task_ids))
    elif tr == TR.ALL_SUCCESS:
        num_failures = upstream - successes
        if num_failures > 0:
            yield self._failing_status(reason="Task's trigger rule '{0}' requires all upstream tasks to have succeeded, but found {1} non-success(es). upstream_tasks_state={2}, upstream_task_ids={3}".format(tr, num_failures, upstream_tasks_state, task.upstream_task_ids))
    elif tr == TR.ALL_FAILED:
        num_successes = upstream - failed - upstream_failed
        if num_successes > 0:
            yield self._failing_status(reason="Task's trigger rule '{0}' requires all upstream tasks to have failed, but found {1} non-failure(s). upstream_tasks_state={2}, upstream_task_ids={3}".format(tr, num_successes, upstream_tasks_state, task.upstream_task_ids))
    elif tr == TR.ALL_DONE:
        if not upstream_done:
            yield self._failing_status(reason="Task's trigger rule '{0}' requires all upstream tasks to have completed, but found {1} task(s) that weren't done. upstream_tasks_state={2}, upstream_task_ids={3}".format(tr, upstream_done, upstream_tasks_state, task.upstream_task_ids))
    elif tr == TR.NONE_FAILED:
        num_failures = upstream - successes - skipped
        if num_failures > 0:
            yield self._failing_status(reason="Task's trigger rule '{0}' requires all upstream tasks to have succeeded or been skipped, but found {1} non-success(es). upstream_tasks_state={2}, upstream_task_ids={3}".format(tr, num_failures, upstream_tasks_state, task.upstream_task_ids))
    elif tr == TR.NONE_SKIPPED:
        if skipped > 0:
            yield self._failing_status(reason="Task's trigger rule '{0}' requires all upstream tasks to not have been skipped, but found {1} task(s) skipped. upstream_tasks_state={2}, upstream_task_ids={3}".format(tr, skipped, upstream_tasks_state, task.upstream_task_ids))
    else:
        yield self._failing_status(reason="No strategy to evaluate trigger rule '{0}'.".format(tr))