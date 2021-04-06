# Given an integer array nums, find the contiguous subarray(containing at least one number) which has the largest sum and return its sum.

# i番目までの合計とi番目の数の大きい方をcurr_sumに入れる
# max_numでそれまでで最も大きかったcurr_numを保存する
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        curr_sum = max_sum = nums[0]

        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum
