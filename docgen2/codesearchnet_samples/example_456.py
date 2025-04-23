def get_attachments_by_name(self, name, check_regex, find_first=False):
    attachments = []
    for part in self.mail.walk():
        mail_part = MailPart(part)
        if mail_part.is_attachment():
            found_attachment = mail_part.has_matching_name(name) if check_regex else mail_part.has_equal_name(name)
            if found_attachment:
                (file_name, file_payload) = mail_part.get_file()
                self.log.info('Found attachment: {}'.format(file_name))
                attachments.append((file_name, file_payload))
                if find_first:
                    break
    return attachments