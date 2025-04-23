def has_mail_attachment(self, name, mail_folder='INBOX', check_regex=False):
    mail_attachments = self._retrieve_mails_attachments_by_name(name, mail_folder, check_regex, latest_only=True)
    return len(mail_attachments) > 0