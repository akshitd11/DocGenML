def recognize_speech(self, config, audio, retry=None, timeout=None):
    client = self.get_conn()
    response = client.recognize(config=config, audio=audio, retry=retry, timeout=timeout)
    self.log.info('Recognised speech: %s' % response)
    return response