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
