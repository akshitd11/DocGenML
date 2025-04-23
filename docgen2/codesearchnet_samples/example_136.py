def run(self, hql, parameters=None):
    return super().run(self._strip_sql(hql), parameters)