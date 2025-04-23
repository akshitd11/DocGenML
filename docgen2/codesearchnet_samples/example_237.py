def import_from_storage_bucket(self, bucket, file, namespace=None, entity_filter=None, labels=None):
    admin_conn = self.get_conn()
    input_url = 'gs://' + '/'.join(filter(None, [bucket, namespace, file]))
    if not entity_filter:
        entity_filter = {}
    if not labels:
        labels = {}
    body = {'inputUrl': input_url, 'entityFilter': entity_filter, 'labels': labels}
    resp = admin_conn.projects().import_(projectId=self.project_id, body=body).execute(num_retries=self.num_retries)
    return resp