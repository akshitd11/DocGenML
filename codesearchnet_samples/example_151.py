def get_function(self, name):
    return self.get_conn().projects().locations().functions().get(name=name).execute(num_retries=self.num_retries)