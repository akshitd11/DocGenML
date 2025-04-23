def send_email(to, subject, html_content, files=None, dryrun=False, cc=None, bcc=None, mime_subtype='mixed', sandbox_mode=False, **kwargs):
    if files is None:
        files = []
    mail = Mail()
    from_email = kwargs.get('from_email') or os.environ.get('SENDGRID_MAIL_FROM')
    from_name = kwargs.get('from_name') or os.environ.get('SENDGRID_MAIL_SENDER')
    mail.from_email = Email(from_email, from_name)
    mail.subject = subject
    mail.mail_settings = MailSettings()
    if sandbox_mode:
        mail.mail_settings.sandbox_mode = SandBoxMode(enable=True)
    personalization = Personalization()
    to = get_email_address_list(to)
    for to_address in to:
        personalization.add_to(Email(to_address))
    if cc:
        cc = get_email_address_list(cc)
        for cc_address in cc:
            personalization.add_cc(Email(cc_address))
    if bcc:
        bcc = get_email_address_list(bcc)
        for bcc_address in bcc:
            personalization.add_bcc(Email(bcc_address))
    pers_custom_args = kwargs.get('personalization_custom_args', None)
    if isinstance(pers_custom_args, dict):
        for key in pers_custom_args.keys():
            personalization.add_custom_arg(CustomArg(key, pers_custom_args[key]))
    mail.add_personalization(personalization)
    mail.add_content(Content('text/html', html_content))
    categories = kwargs.get('categories', [])
    for cat in categories:
        mail.add_category(Category(cat))
    for fname in files:
        basename = os.path.basename(fname)
        attachment = Attachment()
        attachment.type = mimetypes.guess_type(basename)[0]
        attachment.filename = basename
        attachment.disposition = 'attachment'
        attachment.content_id = '<{0}>'.format(basename)
        with open(fname, 'rb') as f:
            attachment.content = base64.b64encode(f.read()).decode('utf-8')
        mail.add_attachment(attachment)
    _post_sendgrid_mail(mail.get())