from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor: return image

        # 移動範囲(上、下、右、左)の網羅
        neis = [[0,1],[0,-1],[1,0],[-1,0]]
        m = len(image)
        n = len(image[0])

        def bfs(row, col, oldColor):
            q = [[row, col]]
            while q:
                x_, y_ = q.pop(0)
                # 起点マスの周辺を全部精査 => qがあればwhileを繰り返す(BFS)
                for nei in neis:
                    x = x_+nei[0]
                    y = y_+nei[1]
                    inSquare = True if x < m and x >= 0 and y < n and y >= 0 else False
                    if inSquare and image[x][y] == oldColor:
                        image[x][y] = newColor
                        q.append([x, y])

        def dfs(row, col, oldColor):
            #　4-firectionallyの精査
            for nei in neis:
                # 1マス移動
                x = row + nei[0]
                y = col + nei[1]
                inSquare = True if x < m and x >= 0 and y < n and y >= 0 else False

                if inSquare and image[x][y] == oldColor:
                    image[x][y] = newColor
                    # 移動先から再度DFS
                    dfs(x,y,oldColor)

        oldColor = image[sr][sc]
        # 起点マスの色を最初に変更
        image[sr][sc] = newColor
        dfs(sr,sc,oldColor)
        return image

