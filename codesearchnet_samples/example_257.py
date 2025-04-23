def render_log_filename(ti, try_number, filename_template):
    (filename_template, filename_jinja_template) = parse_template_string(filename_template)
    if filename_jinja_template:
        jinja_context = ti.get_template_context()
        jinja_context['try_number'] = try_number
        return filename_jinja_template.render(**jinja_context)
    return filename_template.format(dag_id=ti.dag_id, task_id=ti.task_id, execution_date=ti.execution_date.isoformat(), try_number=try_number)