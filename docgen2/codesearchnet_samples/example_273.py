def create_version(self, project_id, model_name, version_spec):
    parent_name = 'projects/{}/models/{}'.format(project_id, model_name)
    create_request = self._mlengine.projects().models().versions().create(parent=parent_name, body=version_spec)
    response = create_request.execute()
    get_request = self._mlengine.projects().operations().get(name=response['name'])
    return _poll_with_exponential_delay(request=get_request, max_n=9, is_done_func=lambda resp: resp.get('done', False), is_error_func=lambda resp: resp.get('error', None) is not None)