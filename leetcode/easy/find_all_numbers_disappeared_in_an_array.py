from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        rangeList = [i for i in range(1, len(nums)+1)]
        result = set(rangeList) - set(nums)

        return result
