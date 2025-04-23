def validate(self, body_to_validate):
    try:
        for validation_spec in self._validation_specs:
            self._validate_field(validation_spec=validation_spec, dictionary_to_validate=body_to_validate)
    except GcpFieldValidationException as e:
        raise GcpFieldValidationException("There was an error when validating: body '{}': '{}'".format(body_to_validate, e))
    all_field_names = [spec['name'] for spec in self._validation_specs if spec.get('type') != 'union' and spec.get('api_version') != self._api_version]
    all_union_fields = [spec for spec in self._validation_specs if spec.get('type') == 'union']
    for union_field in all_union_fields:
        all_field_names.extend([nested_union_spec['name'] for nested_union_spec in union_field['fields'] if nested_union_spec.get('type') != 'union' and nested_union_spec.get('api_version') != self._api_version])
    for field_name in body_to_validate.keys():
        if field_name not in all_field_names:
            self.log.warning("The field '%s' is in the body, but is not specified in the validation specification '%s'. This might be because you are using newer API version and new field names defined for that version. Then the warning can be safely ignored, or you might want to upgrade the operatorto the version that supports the new API version.", field_name, self._validation_specs)