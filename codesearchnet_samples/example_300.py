def get_state_exitcode_details(self, resource_group, name):
    current_state = self._get_instance_view(resource_group, name).current_state
    return (current_state.state, current_state.exit_code, current_state.detail_status)