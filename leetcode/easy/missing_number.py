from typing import List


# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         maxNum = len(nums)

#         for n in range(0, maxNum+1):
#             if n not in nums:
#                 return n

class Solution:
    def missingNumber(self, nums):
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
