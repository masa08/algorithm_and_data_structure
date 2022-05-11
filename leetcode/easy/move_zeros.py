# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# numsに0が存在した場合、jの位置とi(0が存在する)の位置を入れ替え続けることで、0を後方に持っていく。

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] == 0: continue
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
