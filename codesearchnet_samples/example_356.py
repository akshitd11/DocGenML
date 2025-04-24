def ready_for_retry(self):
    return self.state == State.UP_FOR_RETRY and self.next_retry_datetime() < timezone.utcnow()