def on_error(self, error, items):
    self.log.error('Encountered Segment error: {segment_error} with items: {with_items}'.format(segment_error=error, with_items=items))
    raise AirflowException('Segment error: {}'.format(error))