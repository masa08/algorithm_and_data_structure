# TODO: 説明文章書けるようにする
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(cur, cur_sum, idx):
            if cur_sum > target:
                return
            if cur_sum == target:
                ans.append(cur)
                return
            for i in range(idx, len(candidates)):
                dfs(cur + [candidates[i]], cur_sum + candidates[i], i)

        dfs([], 0, 0)

        return ans


if __name__ == '__main__':
    target = Solution()
    print(target.combinationSum([2, 3, 6, 7], 7))
