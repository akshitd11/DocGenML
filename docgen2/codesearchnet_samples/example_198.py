def _find_zombies(self, session):
    now = timezone.utcnow()
    zombies = []
    if (now - self._last_zombie_query_time).total_seconds() > self._zombie_query_interval:
        from airflow.jobs import LocalTaskJob as LJ
        self.log.info("Finding 'running' jobs without a recent heartbeat")
        TI = airflow.models.TaskInstance
        limit_dttm = timezone.utcnow() - timedelta(seconds=self._zombie_threshold_secs)
        self.log.info('Failing jobs without heartbeat after %s', limit_dttm)
        tis = session.query(TI).join(LJ, TI.job_id == LJ.id).filter(TI.state == State.RUNNING).filter(or_(LJ.state != State.RUNNING, LJ.latest_heartbeat < limit_dttm)).all()
        self._last_zombie_query_time = timezone.utcnow()
        for ti in tis:
            zombies.append(SimpleTaskInstance(ti))
    return zombies