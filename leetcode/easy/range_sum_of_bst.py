# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBSTFast(self, root: TreeNode, L: int, R: int) -> int:
        if root is None: return 0
        # 対象範囲ではないvalの場合は次の処理に移る
        if root.val > R: return self.rangeSumBST(root, L, R)
        if root.val < L: return self.rangeSumBST(root, L, R)
        # 対象範囲のvalであればvalを回帰的に足し合わせてreturnする
        return root.val + self.rangeSumBST(root.left,L,R) + self.rangeSumBST(root.right,L,R)


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
