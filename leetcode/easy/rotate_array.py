from typing import List

# 1. 配列の要素をreverseする
# 2. 0からk-1までの配列の要素をreverseする
# 3. kからlen(nums)-1までの配列の要素をreverseする
# => 求める配列が出力される
class Solution:
  def reverse(self, nums: List[int], l: int, r: int) -> None:
    while l <= r:
      nums[l], nums[r] = nums[r], nums[l]
      l += 1
      r -= 1

  def rotate(self, nums: List[int], k: int) -> None:
    if k > len(nums): k %= len(nums)

    self.reverse(nums, 0, len(nums)-1)
    self.reverse(nums, 0, k-1)
    self.reverse(nums, k, len(nums)-1)
