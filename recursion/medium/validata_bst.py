class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def validateBST(root):
    if root is None: return True
    if root.right and root.data > findMinNode(root.right).data: return False
    if root.left and root.data < findMaxNode(root.left).data: return False
    return validateBSTHelper(root)

def validateBSTHelper(root):
    if root.left is None and root.right is None: return True
    if root.right and root.data > root.right.data: return False
    if root.left and root.data < root.left.data: return False
    right = validateBSTHelper(root.right)
    left = validateBSTHelper(root.left)
    return right and left

def findMinNode(root):
    if root.left is None: return root
    return findMinNode(root.left)

def findMaxNode(root):
    if root.right is None: return root
    return findMaxNode(root.right)
