def cleanup_database_hook(self):
    if self.database_type == 'postgres':
        if hasattr(self.db_hook, 'conn') and self.db_hook.conn and self.db_hook.conn.notices:
            for output in self.db_hook.conn.notices:
                self.log.info(output)