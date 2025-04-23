def send_metric(self, metric_name, datapoint, tags=None, type_=None, interval=None):
    response = api.Metric.send(metric=metric_name, points=datapoint, host=self.host, tags=tags, type=type_, interval=interval)
    self.validate_response(response)
    return response