def template_field_role(app, typ, rawtext, text, lineno, inliner, options={}, content=[]):
    text = utils.unescape(text)
    try:
        template_fields = get_template_field(app.env, text)
    except RoleException as e:
        msg = inliner.reporter.error('invalid class name %s \n%s' % (text, e), line=lineno)
        prb = inliner.problematic(rawtext, rawtext, msg)
        return ([prb], [msg])
    node = nodes.inline(rawtext=rawtext)
    for (i, field) in enumerate(template_fields):
        if i != 0:
            node += nodes.Text(', ')
        node += nodes.literal(field, '', nodes.Text(field))
    return ([node], [])