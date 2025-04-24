def invoke_lambda(self, payload):
    awslambda_conn = self.get_conn()
    response = awslambda_conn.invoke(FunctionName=self.function_name, InvocationType=self.invocation_type, LogType=self.log_type, Payload=payload, Qualifier=self.qualifier)
    return response