def annotate_text(self, document, features, encoding_type=None, retry=None, timeout=None, metadata=None):
    client = self.get_conn()
    return client.annotate_text(document=document, features=features, encoding_type=encoding_type, retry=retry, timeout=timeout, metadata=metadata)