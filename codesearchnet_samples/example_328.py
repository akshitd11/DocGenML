def _get_token(self, token, http_conn_id):
    if token:
        return token
    elif http_conn_id:
        conn = self.get_connection(http_conn_id)
        extra = conn.extra_dejson
        return extra.get('webhook_token', '')
    else:
        raise AirflowException('Cannot get token: No valid Slack webhook token nor conn_id supplied')