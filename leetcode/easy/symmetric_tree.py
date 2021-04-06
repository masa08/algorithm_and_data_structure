# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def _isSymmetric(one, two):
            if(not one and not two):
                return True
            if(not one or not two):
                return False
            if(one.val != two.val):
                return False
            return _isSymmetric(one.left, two.right) and _isSymmetric(one.right, two.left)

        if(not root):
            return True
        return _isSymmetric(root.left, root.right)
