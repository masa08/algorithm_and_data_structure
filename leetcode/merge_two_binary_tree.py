# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursiveな解き方
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 and root2:
            merget_root = TreeNode(root1.val + root2.val)
            merget_root.left = self.mergeTrees(root1.left, root2.left)
            merget_root.right = self.mergeTrees(root1.right, root2.right)

            return merget_root
        else:
            return root1 or root2
