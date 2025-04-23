def wait_for_transfer_job(self, job, expected_statuses=(GcpTransferOperationStatus.SUCCESS,), timeout=60):
    while timeout > 0:
        operations = self.list_transfer_operations(filter={FILTER_PROJECT_ID: job[PROJECT_ID], FILTER_JOB_NAMES: [job[NAME]]})
        if GCPTransferServiceHook.operations_contain_expected_statuses(operations, expected_statuses):
            return
        time.sleep(TIME_TO_SLEEP_IN_SECONDS)
        timeout -= TIME_TO_SLEEP_IN_SECONDS
    raise AirflowException('Timeout. The operation could not be completed within the allotted time.')