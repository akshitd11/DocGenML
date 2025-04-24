def execute(self):
    proxies = {}
    if self.proxy:
        proxies = {'https': self.proxy}
    slack_message = self._build_slack_message()
    self.run(endpoint=self.webhook_token, data=slack_message, headers={'Content-type': 'application/json'}, extra_options={'proxies': proxies})