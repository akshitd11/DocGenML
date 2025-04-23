def is_bucket_updated(self, current_num_objects):
    if current_num_objects > self.previous_num_objects:
        self.log.info('\n                New objects found at {} resetting last_activity_time.\n                '.format(os.path.join(self.bucket, self.prefix)))
        self.last_activity_time = get_time()
        self.inactivity_seconds = 0
        self.previous_num_objects = current_num_objects
    elif current_num_objects < self.previous_num_objects:
        if self.allow_delete:
            self.previous_num_objects = current_num_objects
            self.last_activity_time = get_time()
            self.log.warning('\n                    Objects were deleted during the last\n                    poke interval. Updating the file counter and\n                    resetting last_activity_time.\n                    ')
        else:
            raise RuntimeError('\n                    Illegal behavior: objects were deleted in {} between pokes.\n                    '.format(os.path.join(self.bucket, self.prefix)))
    else:
        if self.last_activity_time:
            self.inactivity_seconds = (get_time() - self.last_activity_time).total_seconds()
        else:
            self.last_activity_time = get_time()
            self.inactivity_seconds = 0
        if self.inactivity_seconds >= self.inactivity_period:
            if current_num_objects >= self.min_objects:
                self.log.info('\n                        SUCCESS:\n                        Sensor found {} objects at {}.\n                        Waited at least {} seconds, with no new objects dropped.\n                        '.format(current_num_objects, os.path.join(self.bucket, self.prefix), self.inactivity_period))
                return True
            warn_msg = '\n                    FAILURE:\n                    Inactivity Period passed,\n                    not enough objects found in {}\n                    '.format(os.path.join(self.bucket, self.prefix))
            self.log.warning(warn_msg)
            return False
        return False