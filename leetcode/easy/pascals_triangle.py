from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lists = []
        for i in range(numRows):
            lists.append([1]*(i+1))
            if i >= 2:
                # 0,-1以外の全て
                for j in range(1, i):
                    lists[i][j] = lists[i-1][j-1]+lists[i-1][j]
        return lists
