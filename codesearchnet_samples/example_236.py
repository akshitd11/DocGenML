def export_to_storage_bucket(self, bucket, namespace=None, entity_filter=None, labels=None):
    admin_conn = self.get_conn()
    output_uri_prefix = 'gs://' + '/'.join(filter(None, [bucket, namespace]))
    if not entity_filter:
        entity_filter = {}
    if not labels:
        labels = {}
    body = {'outputUrlPrefix': output_uri_prefix, 'entityFilter': entity_filter, 'labels': labels}
    resp = admin_conn.projects().export(projectId=self.project_id, body=body).execute(num_retries=self.num_retries)
    return resp