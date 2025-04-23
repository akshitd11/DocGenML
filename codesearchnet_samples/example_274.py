def set_default_version(self, project_id, model_name, version_name):
    full_version_name = 'projects/{}/models/{}/versions/{}'.format(project_id, model_name, version_name)
    request = self._mlengine.projects().models().versions().setDefault(name=full_version_name, body={})
    try:
        response = request.execute()
        self.log.info('Successfully set version: %s to default', response)
        return response
    except HttpError as e:
        self.log.error('Something went wrong: %s', e)
        raise