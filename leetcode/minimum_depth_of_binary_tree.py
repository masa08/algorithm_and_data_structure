# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# TODO: BFSとDFSのいい練習になりそうなので復習する
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if left == 0:
                return right+1
            if right == 0:
                return left+1
            return min(left, right)+1
        return dfs(root)
