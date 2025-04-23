def download_mail_attachments(self, name, local_output_directory, mail_folder='INBOX', check_regex=False, latest_only=False, not_found_mode='raise'):
    mail_attachments = self._retrieve_mails_attachments_by_name(name, mail_folder, check_regex, latest_only)
    if not mail_attachments:
        self._handle_not_found_mode(not_found_mode)
    self._create_files(mail_attachments, local_output_directory)