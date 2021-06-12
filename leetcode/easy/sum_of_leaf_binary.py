# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.total = 0

        def _sumRootToLeaf(root,nums):
            if not root.left and not root.right:
                nums += str(root.val)
                self.total += int(nums,2)
                return
            nums += str(root.val)
            if root.left:
                _sumRootToLeaf(root.left,nums)
            if root.right:
                _sumRootToLeaf(root.right,nums)

        _sumRootToLeaf(root, "")
        return self.total
