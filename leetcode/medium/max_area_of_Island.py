# https://www.youtube.com/watch?v=jbeRlfKxo60
# https://leetcode.com/problems/number-of-islands/
import itertools
from typing import List


class SolutionDFS:
    def maxAreaOfIsland(self, G: List[List[int]]) -> int:
        M, N, maxArea = len(G), len(G[0]), 0

        def dfs_area(x, y):
            G[x][y] = 0
            V.add((x, y))
            for i, j in [[x-1, y], [x, y+1], [x+1, y], [x, y-1]]:
                # islandをはみ出した場合、0でない場合は処理しない
                if not (i in [-1, M] or j in [-1, N] or G[i][j] == 0):
                    dfs_area(i, j)

        for i, j in itertools.product(range(M), range(N)):
            if G[i][j] == 1:
                V = set()
                dfs_area(i, j)
                maxArea = max(maxArea, len(V))
        return maxArea


class SolutionBFS:
    def maxAreaOfIsland(self, G: List[List[int]]) -> int:
        M, N, maxArea = len(G), len(G[0]), 0

        def bfs_area(x, y):
            queue, target, ans, G[x][y] = [[x, y]], [], 1, 0
            while queue:
                for i, j in queue:
                    for k, l in [[i-1, j], [i, j+1], [i+1, j], [i, j-1]]:
                        # islandをはみ出した場合と、0の場合はcontinue
                        if k in [-1, M] or l in [-1, N] or G[k][l] == 0:
                            continue
                        # 次回探索候補tをpに代入、次回探索に影響ないようにtを初期化
                        ans += 1
                        G[k][l] = 0
                        target.append([k, l])
                queue, target = target, []
            return ans

        for i, j in itertools.product(range(M), range(N)):
            if G[i][j] == 1:
                maxArea = max(maxArea, bfs_area(i, j))
        return maxArea
