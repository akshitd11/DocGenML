def classify_text(self, document, retry=None, timeout=None, metadata=None):
    client = self.get_conn()
    return client.classify_text(document=document, retry=retry, timeout=timeout, metadata=metadata)