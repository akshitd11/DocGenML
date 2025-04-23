def query_metric(self, query, from_seconds_ago, to_seconds_ago):
    now = int(time.time())
    response = api.Metric.query(start=now - from_seconds_ago, end=now - to_seconds_ago, query=query)
    self.validate_response(response)
    return response