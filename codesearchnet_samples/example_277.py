def create_model(self, project_id, model):
    if not model['name']:
        raise ValueError('Model name must be provided and could not be an empty string')
    project = 'projects/{}'.format(project_id)
    request = self._mlengine.projects().models().create(parent=project, body=model)
    return request.execute()