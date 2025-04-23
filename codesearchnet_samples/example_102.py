def _get_error_code(self, e):
    try:
        matches = self.error_code_pattern.match(str(e))
        code = int(matches.group(0))
        return code
    except ValueError:
        return e