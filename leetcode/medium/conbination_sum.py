# TODO: 説明文章書けるようにする
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)

        # cur = 現在の配列の要素, cur_sum = 現在の配列の中身の合計
        def dfs(cur, cur_sum, idx):
            if cur_sum > target:
                return
            if cur_sum == target:
                ans.append(cur)
                return
            for i in range(idx, n):
                dfs(cur + [candidates[i]], cur_sum + candidates[i], i)

        dfs([], 0, 0)

        return ans
