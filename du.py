def du(node):
    result = [
        (get_name(child), get_size(child)) for child in get_children(node)
        ]
    result.sort(key=lambda elem: elem[1], reverse=True)
    return result


def get_size(node):
    if is_file(node):
        return get_meta(node)['size']
    return sum(get_size(child) for child in get_children(node))

