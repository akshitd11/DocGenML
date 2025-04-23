def create_topic(self, project, topic, fail_if_exists=False):
    service = self.get_conn()
    full_topic = _format_topic(project, topic)
    try:
        service.projects().topics().create(name=full_topic, body={}).execute(num_retries=self.num_retries)
    except HttpError as e:
        if str(e.resp['status']) == '409':
            message = 'Topic already exists: {}'.format(full_topic)
            self.log.warning(message)
            if fail_if_exists:
                raise PubSubException(message)
        else:
            raise PubSubException('Error creating topic {}'.format(full_topic), e)