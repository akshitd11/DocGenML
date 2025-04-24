def create_subscription(self, topic_project, topic, subscription=None, subscription_project=None, ack_deadline_secs=10, fail_if_exists=False):
    service = self.get_conn()
    full_topic = _format_topic(topic_project, topic)
    if not subscription:
        subscription = 'sub-{}'.format(uuid4())
    if not subscription_project:
        subscription_project = topic_project
    full_subscription = _format_subscription(subscription_project, subscription)
    body = {'topic': full_topic, 'ackDeadlineSeconds': ack_deadline_secs}
    try:
        service.projects().subscriptions().create(name=full_subscription, body=body).execute(num_retries=self.num_retries)
    except HttpError as e:
        if str(e.resp['status']) == '409':
            message = 'Subscription already exists: {}'.format(full_subscription)
            self.log.warning(message)
            if fail_if_exists:
                raise PubSubException(message)
        else:
            raise PubSubException('Error creating subscription {}'.format(full_subscription), e)
    return subscription