class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # for i in range(1, num+1):
        #     square = i ** 2
        #     if square == num: return True
        #     elif square < num: continue
        #     else: break
        # return False

        # binary search
        low = 1
        high = num
        while low <= high:
            mid = (low+high)//2
            square = mid**2
            if square == num:
                return True
            elif square < num:
                low = mid + 1
            else:
                high = mid - 1
        return False
