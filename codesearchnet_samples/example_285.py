def run_pod(self, pod, startup_timeout=120, get_logs=True):
    resp = self.run_pod_async(pod)
    curr_time = dt.now()
    if resp.status.start_time is None:
        while self.pod_not_started(pod):
            delta = dt.now() - curr_time
            if delta.seconds >= startup_timeout:
                raise AirflowException('Pod took too long to start')
            time.sleep(1)
        self.log.debug('Pod not yet started')
    return self._monitor_pod(pod, get_logs)