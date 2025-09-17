
from itertools import chain


def remove_first_level(tree):
    return list(chain.from_iterable(
        node for node in tree if isinstance(node, list)
    ))
