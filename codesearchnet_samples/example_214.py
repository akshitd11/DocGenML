def operations_contain_expected_statuses(operations, expected_statuses):
    expected_statuses = {expected_statuses} if isinstance(expected_statuses, six.string_types) else set(expected_statuses)
    if len(operations) == 0:
        return False
    current_statuses = {operation[METADATA][STATUS] for operation in operations}
    if len(current_statuses - set(expected_statuses)) != len(current_statuses):
        return True
    if len(NEGATIVE_STATUSES - current_statuses) != len(NEGATIVE_STATUSES):
        raise AirflowException('An unexpected operation status was encountered. Expected: {}'.format(', '.join(expected_statuses)))
    return False