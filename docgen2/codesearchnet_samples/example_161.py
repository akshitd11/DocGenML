def delete_subscription(self, project, subscription, fail_if_not_exists=False):
    service = self.get_conn()
    full_subscription = _format_subscription(project, subscription)
    try:
        service.projects().subscriptions().delete(subscription=full_subscription).execute(num_retries=self.num_retries)
    except HttpError as e:
        if str(e.resp['status']) == '404':
            message = 'Subscription does not exist: {}'.format(full_subscription)
            self.log.warning(message)
            if fail_if_not_exists:
                raise PubSubException(message)
        else:
            raise PubSubException('Error deleting subscription {}'.format(full_subscription), e)