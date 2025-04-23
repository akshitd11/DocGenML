def post_event(self, title, text, aggregation_key=None, alert_type=None, date_happened=None, handle=None, priority=None, related_event_id=None, tags=None, device_name=None):
    response = api.Event.create(title=title, text=text, aggregation_key=aggregation_key, alert_type=alert_type, date_happened=date_happened, handle=handle, priority=priority, related_event_id=related_event_id, tags=tags, host=self.host, device_name=device_name, source_type_name=self.source_type_name)
    self.validate_response(response)
    return response