from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 昇順なので、pivodを取ることによって、root.valueは決定する。
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        pivod = len(nums) // 2

        root = TreeNode(nums[pivod])
        root.left = self.sortedArrayToBST(nums[:pivod])
        root.right = self.sortedArrayToBST(nums[pivod+1:])

        return root
