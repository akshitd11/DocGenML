def clear_nonexistent_import_errors(self, session):
    query = session.query(errors.ImportError)
    if self._file_paths:
        query = query.filter(~errors.ImportError.filename.in_(self._file_paths))
    query.delete(synchronize_session='fetch')
    session.commit()