def closest_ds_partition(table, ds, before=True, schema='default', metastore_conn_id='metastore_default'):
    from airflow.hooks.hive_hooks import HiveMetastoreHook
    if '.' in table:
        (schema, table) = table.split('.')
    hh = HiveMetastoreHook(metastore_conn_id=metastore_conn_id)
    partitions = hh.get_partitions(schema=schema, table_name=table)
    if not partitions:
        return None
    part_vals = [list(p.values())[0] for p in partitions]
    if ds in part_vals:
        return ds
    else:
        parts = [datetime.datetime.strptime(pv, '%Y-%m-%d') for pv in part_vals]
        target_dt = datetime.datetime.strptime(ds, '%Y-%m-%d')
        closest_ds = _closest_date(target_dt, parts, before_target=before)
        return closest_ds.isoformat()