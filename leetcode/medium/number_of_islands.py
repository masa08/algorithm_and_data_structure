import itertools
from typing import List


class Solution:
    def numIslandsBfs(self, grid: List[List[str]]) -> int:
        height, width, count = len(grid), len(grid[0]), 0

        def bfs_search(x, y):
            p, temp, grid[x][y] = [[x, y]], [], 0
            while p:
                for i, j in p:
                    for k, l in [[i-1, j], [i, j+1], [i+1, j], [i, j-1]]:
                        if k in [-1, height] or l in [-1, width] or grid[k][l] == "0":
                            continue
                        grid[k][l] = "0"
                        temp.append([k, l])
                p, temp = temp, []

        for i, j in itertools.product(range(height), range(width)):
            if grid[i][j] == "1":
                bfs_search(i, j)
                count += 1
        return count

    def numIslandsDfs(self, grid: List[List[str]]) -> int:
        height, width, count = len(grid), len(grid[0]), 0

        def dfs_search(x, y):
            grid[x][y] = "0"
            for i, j in [[x-1, y], [x, y+1], [x+1, y], [x, y-1]]:
                if not (i in [-1, height] or j in [-1, width] or grid[i][j] == "0"):
                    dfs_search(i, j)

        for i, j in itertools.product(range(height), range(width)):
            if grid[i][j] == "1":
                dfs_search(i, j)
                count += 1
        return count
