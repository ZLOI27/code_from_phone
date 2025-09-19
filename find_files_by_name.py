def find_files_by_name(node, substr):
    def walk(node, substr, ancestry):
        name = get_name(node)
        ancestry.append(name)
        if is_file(node) and (substr in name):
            return [os.path.join(*ancestry)]
        elif is_file(node):
            return []
        return [walk(child, substr, ancestry[:]) for child in get_children(node)] 

    return flattern(walk(node, substr, []))
