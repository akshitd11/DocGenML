def _build_slack_message(self):
    cmd = {}
    if self.channel:
        cmd['channel'] = self.channel
    if self.username:
        cmd['username'] = self.username
    if self.icon_emoji:
        cmd['icon_emoji'] = self.icon_emoji
    if self.link_names:
        cmd['link_names'] = 1
    if self.attachments:
        cmd['attachments'] = self.attachments
    cmd['text'] = self.message
    return json.dumps(cmd)