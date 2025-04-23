def get_database_hook(self):
    if self.database_type == 'postgres':
        self.db_hook = PostgresHook(postgres_conn_id=self.db_conn_id, schema=self.database)
    else:
        self.db_hook = MySqlHook(mysql_conn_id=self.db_conn_id, schema=self.database)
    return self.db_hook