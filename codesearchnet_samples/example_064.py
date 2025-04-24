def max_partition(table, schema='default', field=None, filter_map=None, metastore_conn_id='metastore_default'):
    from airflow.hooks.hive_hooks import HiveMetastoreHook
    if '.' in table:
        (schema, table) = table.split('.')
    hh = HiveMetastoreHook(metastore_conn_id=metastore_conn_id)
    return hh.max_partition(schema=schema, table_name=table, field=field, filter_map=filter_map)