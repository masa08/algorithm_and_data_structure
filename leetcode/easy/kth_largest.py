
# 回答1
# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.k = k
#         self.nums = nums

#     def add(self, val: int) -> int:
#         self.nums.append(val)
#         self.nums = sorted(self.nums, reverse=True)
#         return self.nums[self.k-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# 回答2
# 上位3つ大きい数を保持し続けて、その配列の[0]要素をreturnする
# heapを用いることにより、sortをしなくて良くなるので、計算量が大幅に改善される
import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
