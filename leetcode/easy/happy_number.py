class Solution:
    def isHappy(self, n: int) -> bool:
        def _calculate(n):
            c = 0
            for i in str(n):
                c += int(i) ** 2
            return c

        if n == 1:
            return True
        seen = []

        while n != 1:
            n = _calculate(n)
            if n in seen:
                return False
            seen.append(n)
        return True
