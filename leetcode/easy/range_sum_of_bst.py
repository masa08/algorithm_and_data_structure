# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        target_num = []

        def _rangeSumBST(root: TreeNode):
            if root is None:
                return
            if low <= root.val and root.val <= high:
                target_num.append(root.val)
            _rangeSumBST(root.left)
            _rangeSumBST(root.right)

        _rangeSumBST(root)
        return sum(target_num)
