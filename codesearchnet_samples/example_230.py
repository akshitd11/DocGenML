def lookup(self, keys, read_consistency=None, transaction=None):
    conn = self.get_conn()
    body = {'keys': keys}
    if read_consistency:
        body['readConsistency'] = read_consistency
    if transaction:
        body['transaction'] = transaction
    resp = conn.projects().lookup(projectId=self.project_id, body=body).execute(num_retries=self.num_retries)
    return resp