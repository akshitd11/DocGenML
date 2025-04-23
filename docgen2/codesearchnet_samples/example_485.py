def execute(self, context):
    self.hook = DiscordWebhookHook(self.http_conn_id, self.webhook_endpoint, self.message, self.username, self.avatar_url, self.tts, self.proxy)
    self.hook.execute()