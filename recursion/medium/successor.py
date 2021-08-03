class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def successor(root,key):
    if root is None: return None
    target = bstSearch(root, key)
    if target.right is not None:
        result = minimumNode(target.right)
        return result
    else:
        result = getNodeMoreThanTarget(root.left, root, target.data)
        if result.data < target.data:
            return None
        else:
            return result

def bstSearch(root,key):
    if root is None: return None
    if root.data == key: return root
    left = bstSearch(root.left, key)
    right = bstSearch(root.right, key)
    return right if right else left

def minimumNode(root):
    if root.left is None: return root
    return minimumNode(root.left)

def getNodeMoreThanTarget(root, prev, targetKey):
    if root.data == targetKey: return prev
    if root.left is None: return root
    result = getNodeMoreThanTarget(root.left, root, targetKey)
    return result

