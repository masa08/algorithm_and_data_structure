# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def _searchBST(root: TreeNode) -> TreeNode:
            if root:
                if root.val == val:
                    return root
                elif root.val < val:
                    return _searchBST(root.right)
                return _searchBST(root.left)
            else:
                return None

        return _searchBST(root)
