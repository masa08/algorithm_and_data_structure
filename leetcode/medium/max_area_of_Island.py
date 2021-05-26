# https://www.youtube.com/watch?v=jbeRlfKxo60
# https://leetcode.com/problems/number-of-islands/
import itertools
from typing import List


class SolutionDFS:
    def maxAreaOfIsland(self, G: List[List[int]]) -> int:
        # 縦の長さ、横の長さを取得, mを初期化
        M, N, m = len(G), len(G[0]), 0

        def dfs_area(x, y):
            if (x, y) in V:
                return
            G[x][y], _ = 0, V.add((x, y))
            # 周辺のマスを探索
            for i, j in [[x-1, y], [x, y+1], [x+1, y], [x, y-1]]:
                # 0の場合とislandをはみ出した場合と0でない場合は処理しない
                if not (i in [-1, M] or j in [-1, N] or G[i][j] == 0):
                    dfs_area(i, j)

        # マスのすべての組み合わせを取得して繰り返し処理
        for i, j in itertools.product(range(M), range(N)):
            # G[i][j]が1であれば処理
            if G[i][j]:
                V = set()
                dfs_area(i, j)
                m = max(m, len(V))
        return m


class SolutionBFS:
    def maxAreaOfIsland(self, G: List[List[int]]) -> int:
        # 縦の長さ、横の長さを取得, mを初期化
        M, N, m = len(G), len(G[0]), 0

        def area(x, y):
            # p = point, t = target, a = answer的なニュアンス
            p, t, a, G[x][y] = [[x, y]], [], 1, 0
            while p:
                for i, j in p:
                    # 周辺のマスを探索
                    for k, l in [[i-1, j], [i, j+1], [i+1, j], [i, j-1]]:
                        # 0の場合とislandをはみ出した場合は次へ
                        if k in [-1, M] or l in [-1, N] or G[k][l] == 0:
                            continue
                        # 次回探索候補tをpに代入、次回探索に影響ないようにtを初期化
                        a, G[k][l], _ = a + 1, 0, t.append([k, l])
                p, t = t, []
            return a
        # マスのすべての組み合わせを取得して繰り返し処理
        for i, j in itertools.product(range(M), range(N)):
            # G[i][j]が1であれば処理
            if G[i][j]:
                m = max(m, area(i, j))
        return m
