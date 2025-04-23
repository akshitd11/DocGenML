def publish_to_target(self, target_arn, message):
    conn = self.get_conn()
    messages = {'default': message}
    return conn.publish(TargetArn=target_arn, Message=json.dumps(messages), MessageStructure='json')