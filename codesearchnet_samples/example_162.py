def pull(self, project, subscription, max_messages, return_immediately=False):
    service = self.get_conn()
    full_subscription = _format_subscription(project, subscription)
    body = {'maxMessages': max_messages, 'returnImmediately': return_immediately}
    try:
        response = service.projects().subscriptions().pull(subscription=full_subscription, body=body).execute(num_retries=self.num_retries)
        return response.get('receivedMessages', [])
    except HttpError as e:
        raise PubSubException('Error pulling messages from subscription {}'.format(full_subscription), e)