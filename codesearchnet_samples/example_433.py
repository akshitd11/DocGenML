def describe_object(self, obj):
    conn = self.get_conn()
    return conn.__getattr__(obj).describe()