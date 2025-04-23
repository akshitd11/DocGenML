def get_file(self):
    return (self.part.get_filename(), self.part.get_payload(decode=True))