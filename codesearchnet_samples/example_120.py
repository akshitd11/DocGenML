def _set_env_from_extras(self, extras):
    key_path = self._get_field(extras, 'key_path', False)
    keyfile_json_str = self._get_field(extras, 'keyfile_dict', False)
    if not key_path and (not keyfile_json_str):
        self.log.info('Using gcloud with application default credentials.')
    elif key_path:
        os.environ[G_APP_CRED] = key_path
    else:
        service_key = tempfile.NamedTemporaryFile(delete=False)
        service_key.write(keyfile_json_str)
        os.environ[G_APP_CRED] = service_key.name
        return service_key