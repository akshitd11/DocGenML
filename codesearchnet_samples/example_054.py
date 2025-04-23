def get_event_buffer(self, dag_ids=None):
    cleared_events = dict()
    if dag_ids is None:
        cleared_events = self.event_buffer
        self.event_buffer = dict()
    else:
        for key in list(self.event_buffer.keys()):
            (dag_id, _, _, _) = key
            if dag_id in dag_ids:
                cleared_events[key] = self.event_buffer.pop(key)
    return cleared_events