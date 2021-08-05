class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def predecessor(root,key):
    if root is None: return None
    target = findNode(root, key)

    if target.left is not None: return maximunNode(target.left)

    predecessor = None
    iterator = root
    while iterator is not None:
        if target.data == iterator.data: return predecessor

        if target.data < iterator.data: iterator = iterator.left
        else:
            predecessor = iterator
            iterator = iterator.right
    return predecessor


def findNode(root, key):
    iterator = root
    while iterator is not None:
        if iterator.data == key: return iterator
        if iterator.data < key: iterator = iterator.right
        else: iterator = iterator.left
    return iterator

def maximunNode(root):
    iterator = root
    while iterator is not None and iterator.right is not None: iterator = iterator.right
    return iterator
