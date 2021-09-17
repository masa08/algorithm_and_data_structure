class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        numbers = []
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                numbers.append(mat[row][col])
        if r * c != len(numbers):
            return mat

        result = []
        index = 0
        for nrow in range(r):
            result.append([])
            for ncol in range(c):
                result[nrow].append(numbers[index])
                index += 1

        return result
