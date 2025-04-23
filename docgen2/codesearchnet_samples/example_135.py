def get_pandas_df(self, hql, parameters=None):
    import pandas
    cursor = self.get_cursor()
    try:
        cursor.execute(self._strip_sql(hql), parameters)
        data = cursor.fetchall()
    except DatabaseError as e:
        raise PrestoException(self._get_pretty_exception_message(e))
    column_descriptions = cursor.description
    if data:
        df = pandas.DataFrame(data)
        df.columns = [c[0] for c in column_descriptions]
    else:
        df = pandas.DataFrame()
    return df