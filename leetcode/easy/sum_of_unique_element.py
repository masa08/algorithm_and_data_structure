from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        org = {}
        result = 0

        for i in nums:
            if i not in org:
                org[i] = 1
            else:
                org[i] += 1

        for k, v in org.items():
            if v == 1:
                result += k

        return result
