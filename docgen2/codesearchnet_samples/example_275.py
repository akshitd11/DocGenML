def list_versions(self, project_id, model_name):
    result = []
    full_parent_name = 'projects/{}/models/{}'.format(project_id, model_name)
    request = self._mlengine.projects().models().versions().list(parent=full_parent_name, pageSize=100)
    response = request.execute()
    next_page_token = response.get('nextPageToken', None)
    result.extend(response.get('versions', []))
    while next_page_token is not None:
        next_request = self._mlengine.projects().models().versions().list(parent=full_parent_name, pageToken=next_page_token, pageSize=100)
        response = next_request.execute()
        next_page_token = response.get('nextPageToken', None)
        result.extend(response.get('versions', []))
        time.sleep(5)
    return result