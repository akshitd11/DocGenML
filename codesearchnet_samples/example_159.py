def delete_topic(self, project, topic, fail_if_not_exists=False):
    service = self.get_conn()
    full_topic = _format_topic(project, topic)
    try:
        service.projects().topics().delete(topic=full_topic).execute(num_retries=self.num_retries)
    except HttpError as e:
        if str(e.resp['status']) == '404':
            message = 'Topic does not exist: {}'.format(full_topic)
            self.log.warning(message)
            if fail_if_not_exists:
                raise PubSubException(message)
        else:
            raise PubSubException('Error deleting topic {}'.format(full_topic), e)