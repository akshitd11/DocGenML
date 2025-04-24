def poke(self, context):
    self.log.info('RedisPubSubSensor checking for message on channels: %s', self.channels)
    message = self.pubsub.get_message()
    self.log.info('Message %s from channel %s', message, self.channels)
    if message and message['type'] == 'message':
        context['ti'].xcom_push(key='message', value=message)
        self.pubsub.unsubscribe(self.channels)
        return True
    return False