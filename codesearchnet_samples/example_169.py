def expand_role(self, role):
    if '/' in role:
        return role
    else:
        return self.get_client_type('iam').get_role(RoleName=role)['Role']['Arn']