def execute(self, context):
    self.hook = self.get_hook()
    self.hook.get_conn()
    self.query_execution_context['Database'] = self.database
    self.result_configuration['OutputLocation'] = self.output_location
    self.query_execution_id = self.hook.run_query(self.query, self.query_execution_context, self.result_configuration, self.client_request_token)
    query_status = self.hook.poll_query_status(self.query_execution_id, self.max_tries)
    if query_status in AWSAthenaHook.FAILURE_STATES:
        raise Exception('Final state of Athena job is {}, query_execution_id is {}.'.format(query_status, self.query_execution_id))
    elif not query_status or query_status in AWSAthenaHook.INTERMEDIATE_STATES:
        raise Exception('Final state of Athena job is {}. Max tries of poll status exceeded, query_execution_id is {}.'.format(query_status, self.query_execution_id))