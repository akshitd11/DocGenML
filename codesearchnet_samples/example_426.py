def _create_cgroup(self, path):
    node = trees.Tree().root
    path_split = path.split(os.sep)
    for path_element in path_split:
        name_to_node = {x.name: x for x in node.children}
        if path_element not in name_to_node:
            self.log.debug('Creating cgroup %s in %s', path_element, node.path)
            node = node.create_cgroup(path_element)
        else:
            self.log.debug('Not creating cgroup %s in %s since it already exists', path_element, node.path)
            node = name_to_node[path_element]
    return node