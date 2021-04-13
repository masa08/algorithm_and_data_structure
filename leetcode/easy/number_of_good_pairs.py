from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairsNum = 0

        for i, num in enumerate(nums):
            targetNums = nums[i+1:]
            if num in targetNums:
                pairsNum += targetNums.count(num)

        return pairsNum
