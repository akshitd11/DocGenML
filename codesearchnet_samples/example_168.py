def get_credentials(self, region_name=None):
    (session, _) = self._get_credentials(region_name)
    return session.get_credentials().get_frozen_credentials()