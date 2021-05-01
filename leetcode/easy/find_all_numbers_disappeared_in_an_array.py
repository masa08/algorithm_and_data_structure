from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 1..nまででnumsに存在する部分は全て負の値にする
        for num in nums:
            ans = abs(num) - 1
            if nums[ans] > 0:
                nums[ans] *= -1

        # 負の値でない部分を返す
        return [i+1 for i in range(len(nums)) if nums[i] > 0]
# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         rangeList = [i for i in range(1, len(nums)+1)]
#         result = set(rangeList) - set(nums)

#         return result
