def analyze_entities(self, document, encoding_type=None, retry=None, timeout=None, metadata=None):
    client = self.get_conn()
    return client.analyze_entities(document=document, encoding_type=encoding_type, retry=retry, timeout=timeout, metadata=metadata)