def upload_function_zip(self, location, zip_path, project_id=None):
    response = self.get_conn().projects().locations().functions().generateUploadUrl(parent=self._full_location(project_id, location)).execute(num_retries=self.num_retries)
    upload_url = response.get('uploadUrl')
    with open(zip_path, 'rb') as fp:
        requests.put(url=upload_url, data=fp, headers={'Content-type': 'application/zip', 'x-goog-content-length-range': '0,104857600'})
    return upload_url