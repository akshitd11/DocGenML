def publish(self, project, topic, messages):
    body = {'messages': messages}
    full_topic = _format_topic(project, topic)
    request = self.get_conn().projects().topics().publish(topic=full_topic, body=body)
    try:
        request.execute(num_retries=self.num_retries)
    except HttpError as e:
        raise PubSubException('Error publishing to topic {}'.format(full_topic), e)