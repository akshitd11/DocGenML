def _delete_cgroup(self, path):
    node = trees.Tree().root
    path_split = path.split('/')
    for path_element in path_split:
        name_to_node = {x.name: x for x in node.children}
        if path_element not in name_to_node:
            self.log.warning('Cgroup does not exist: %s', path)
            return
        else:
            node = name_to_node[path_element]
    parent = node.parent
    self.log.debug('Deleting cgroup %s/%s', parent, node.name)
    parent.delete_cgroup(node.name)