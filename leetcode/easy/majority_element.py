from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        for i in set(nums):
            if counter.get(i) > len(nums)//2:
                return i
