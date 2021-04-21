class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n

        while left <= right:
            mid = (left + right) // 2
            # mid_valueはその値までのrowをfullyにするまでに必要なコインの枚数
            mid_value = (mid * (mid + 1)) // 2

            if mid_value == n:
                return mid
            elif mid_value < n:
                left = mid + 1
            else:
                right = mid - 1
        # なぜrightを返すのか
        return right
