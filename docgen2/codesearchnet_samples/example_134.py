def get_records(self, hql, parameters=None):
    try:
        return super().get_records(self._strip_sql(hql), parameters)
    except DatabaseError as e:
        raise PrestoException(self._get_pretty_exception_message(e))