class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def bstInsert(root,key):
    iterator = root
    while iterator is not None:
        if iterator.data < key and iterator.right is None:
            iterator.right = BinaryTree(key)
        elif iterator.data > key and iterator.left is None:
            iterator.left = BinaryTree(key)
        iterator = iterator.right if iterator.data < key else iterator.left
    return root
