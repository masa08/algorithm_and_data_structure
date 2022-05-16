# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursiveな解き方
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1 or not root2: return root1 or root2

        merge_root = TreeNode(root1.val + root2.val)
        merge_root.left = self.mergeTrees(root1.left, root2.left)
        merge_root.right = self.mergeTrees(root1.right, root2.right)
        return merge_root
