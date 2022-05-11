from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # cache pattern
        # seen = {}
        # for i, v in enumerate(numbers):
        #     remaining = target - v
        #     if remaining in seen:
        #         return [seen[remaining], i + 1]
        #     seen[v] = i + 1
        # return []

        # two pointer pattern
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        return []
