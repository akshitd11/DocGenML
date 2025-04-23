def _query_mssql(self):
    mssql = MsSqlHook(mssql_conn_id=self.mssql_conn_id)
    conn = mssql.get_conn()
    cursor = conn.cursor()
    cursor.execute(self.sql)
    return cursor