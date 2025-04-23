def acknowledge(self, project, subscription, ack_ids):
    service = self.get_conn()
    full_subscription = _format_subscription(project, subscription)
    try:
        service.projects().subscriptions().acknowledge(subscription=full_subscription, body={'ackIds': ack_ids}).execute(num_retries=self.num_retries)
    except HttpError as e:
        raise PubSubException('Error acknowledging {} messages pulled from subscription {}'.format(len(ack_ids), full_subscription), e)