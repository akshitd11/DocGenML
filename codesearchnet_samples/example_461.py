def send_email_smtp(to, subject, html_content, files=None, dryrun=False, cc=None, bcc=None, mime_subtype='mixed', mime_charset='utf-8', **kwargs):
    smtp_mail_from = configuration.conf.get('smtp', 'SMTP_MAIL_FROM')
    to = get_email_address_list(to)
    msg = MIMEMultipart(mime_subtype)
    msg['Subject'] = subject
    msg['From'] = smtp_mail_from
    msg['To'] = ', '.join(to)
    recipients = to
    if cc:
        cc = get_email_address_list(cc)
        msg['CC'] = ', '.join(cc)
        recipients = recipients + cc
    if bcc:
        bcc = get_email_address_list(bcc)
        recipients = recipients + bcc
    msg['Date'] = formatdate(localtime=True)
    mime_text = MIMEText(html_content, 'html', mime_charset)
    msg.attach(mime_text)
    for fname in files or []:
        basename = os.path.basename(fname)
        with open(fname, 'rb') as f:
            part = MIMEApplication(f.read(), Name=basename)
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename
            part['Content-ID'] = '<%s>' % basename
            msg.attach(part)
    send_MIME_email(smtp_mail_from, recipients, msg, dryrun)