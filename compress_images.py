import copy


def compress_images(tree):
    new_meta = copy.deepcopy(get_meta(tree))
    new_children = [
        get_compressed_image(child) if is_jpg_image(child) else child
        for child in get_children(tree)
    ]
    return mkdir(get_name(tree), new_children, new_meta)


def is_jpg_image(child):
    if get_name(child).endswith('.jpg') and is_file(child):
        return True
    return False


def get_compressed_image(child):
    new_meta = copy.deepcopy(get_meta(child))
    new_meta['size'] //= 2
    return mkfile(get_name(child), new_meta)

