def _validate_field(self, validation_spec, dictionary_to_validate, parent=None, force_optional=False):
    field_name = validation_spec['name']
    field_type = validation_spec.get('type')
    optional = validation_spec.get('optional')
    regexp = validation_spec.get('regexp')
    allow_empty = validation_spec.get('allow_empty')
    children_validation_specs = validation_spec.get('fields')
    required_api_version = validation_spec.get('api_version')
    custom_validation = validation_spec.get('custom_validation')
    full_field_path = self._get_field_name_with_parent(field_name=field_name, parent=parent)
    if required_api_version and required_api_version != self._api_version:
        self.log.debug("Skipping validation of the field '%s' for API version '%s' as it is only valid for API version '%s'", field_name, self._api_version, required_api_version)
        return False
    value = dictionary_to_validate.get(field_name)
    if (optional or force_optional) and value is None:
        self.log.debug("The optional field '%s' is missing. That's perfectly OK.", full_field_path)
        return False
    self._sanity_checks(children_validation_specs=children_validation_specs, field_type=field_type, full_field_path=full_field_path, regexp=regexp, allow_empty=allow_empty, custom_validation=custom_validation, value=value)
    if allow_empty is False:
        self._validate_is_empty(full_field_path, value)
    if regexp:
        self._validate_regexp(full_field_path, regexp, value)
    elif field_type == 'dict':
        if not isinstance(value, dict):
            raise GcpFieldValidationException("The field '{}' should be of dictionary type according to the specification '{}' but it is '{}'".format(full_field_path, validation_spec, value))
        if children_validation_specs is None:
            self.log.debug("The dict field '%s' has no nested fields defined in the specification '%s'. That's perfectly ok - it's content will not be validated.", full_field_path, validation_spec)
        else:
            self._validate_dict(children_validation_specs, full_field_path, value)
    elif field_type == 'union':
        if not children_validation_specs:
            raise GcpValidationSpecificationException("The union field '%s' has no nested fields defined in specification '%s'. Unions should have at least one nested field defined.", full_field_path, validation_spec)
        self._validate_union(children_validation_specs, full_field_path, dictionary_to_validate)
    elif field_type == 'list':
        if not isinstance(value, list):
            raise GcpFieldValidationException("The field '{}' should be of list type according to the specification '{}' but it is '{}'".format(full_field_path, validation_spec, value))
    elif custom_validation:
        try:
            custom_validation(value)
        except Exception as e:
            raise GcpFieldValidationException("Error while validating custom field '{}' specified by '{}': '{}'".format(full_field_path, validation_spec, e))
    elif field_type is None:
        self.log.debug("The type of field '%s' is not specified in '%s'. Not validating its content.", full_field_path, validation_spec)
    else:
        raise GcpValidationSpecificationException("The field '{}' is of type '{}' in specification '{}'.This type is unknown to validation!".format(full_field_path, field_type, validation_spec))
    return True