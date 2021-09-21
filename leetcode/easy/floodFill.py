from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        neis = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        m = len(image)
        n = len(image[0])

        def dfs(row, col, oldColor):
            for nei in neis:
                x = row+nei[0]
                y = col+nei[1]
                if x < m and x >= 0 and y < n and y >= 0 and image[x][y] == oldColor:
                    image[x][y] = newColor
                    dfs(x, y, oldColor)

        def bfs(row, col, oldColor):
            q = [[row, col]]
            while q:
                x_, y_ = q.pop(0)
                for nei in neis:
                    x = x_+nei[0]
                    y = y_+nei[1]
                    if x < m and x >= 0 and y < n and y >= 0 and image[x][y] == oldColor:
                        image[x][y] = newColor
                        q.append([x, y])

        if image[sr][sc] == newColor:
            return image
        else:
            oldColor = image[sr][sc]
            image[sr][sc] = newColor
            dfs(sr, sc, oldColor)
            return image
