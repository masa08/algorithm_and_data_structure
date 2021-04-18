from typing import List


# class Solution:
#     def sortArrayByParity(self, A: List[int]) -> List[int]:
#         even = []
#         odd = []
#         for a in A:
#             if a % 2 == 0:
#                 even.append(a)
#             else:
#                 odd.append(a)
#         even.extend(odd)

#         return even

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1
        while i < j:
            # iが奇数で、jが偶数だった場合、数字を入れ替える
            # iに+1をして、jに-1をして、判定を繰り返す。
            if A[i] % 2 == 1 and A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
            i, j = i + 1 - A[i] % 2, j - A[j] % 2
        return A
