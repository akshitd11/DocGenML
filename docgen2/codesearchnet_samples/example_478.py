def _create_dagruns(dag, execution_dates, state, run_id_template):
    drs = DagRun.find(dag_id=dag.dag_id, execution_date=execution_dates)
    dates_to_create = list(set(execution_dates) - set([dr.execution_date for dr in drs]))
    for date in dates_to_create:
        dr = dag.create_dagrun(run_id=run_id_template.format(date.isoformat()), execution_date=date, start_date=timezone.utcnow(), external_trigger=False, state=state)
        drs.append(dr)
    return drs