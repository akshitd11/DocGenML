def run_with_advanced_retry(self, _retry_args, *args, **kwargs):
    self._retry_obj = tenacity.Retrying(**_retry_args)
    self._retry_obj(self.run, *args, **kwargs)