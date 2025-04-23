def _get_cgroup_names():
    with open('/proc/self/cgroup') as f:
        lines = f.readlines()
        d = {}
        for line in lines:
            line_split = line.rstrip().split(':')
            subsystem = line_split[1]
            group_name = line_split[2]
            d[subsystem] = group_name
        return d