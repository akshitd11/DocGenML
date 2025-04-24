def translate(self, values, target_language, format_=None, source_language=None, model=None):
    client = self.get_conn()
    return client.translate(values=values, target_language=target_language, format_=format_, source_language=source_language, model=model)