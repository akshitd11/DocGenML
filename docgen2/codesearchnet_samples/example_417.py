def on_kill(self):
    if self.query_execution_id:
        self.log.info('⚰️⚰️⚰️ Received a kill Signal. Time to Die')
        self.log.info('Stopping Query with executionId - %s', self.query_execution_id)
        response = self.hook.stop_query(self.query_execution_id)
        http_status_code = None
        try:
            http_status_code = response['ResponseMetadata']['HTTPStatusCode']
        except Exception as ex:
            self.log.error('Exception while cancelling query', ex)
        finally:
            if http_status_code is None or http_status_code != 200:
                self.log.error('Unable to request query cancel on athena. Exiting')
            else:
                self.log.info('Polling Athena for query with id %s to reach final state', self.query_execution_id)
                self.hook.poll_query_status(self.query_execution_id)