def du(node):
    return [
        (get_name(child), get_size(child)) for child in get_children(node)
    ]


def get_size(node):
    if is_file(node):
        return get_meta(node)['size']
    return sum(get_size(child) for child in get_children(node))

