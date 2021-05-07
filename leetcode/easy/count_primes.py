# エラトステネスの篩について
# https://math.nakaken88.com/textbook/cp-prime-number-and-composite-number/
# https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%A9%E3%83%88%E3%82%B9%E3%83%86%E3%83%8D%E3%82%B9%E3%81%AE%E7%AF%A9
# https://manabitimes.jp/math/992

class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [False, False] + [True] * (n-2)
        i = 2
        while(i**2 < n):
            if(isPrime[i]):
                j = i**2
                while(j < n):
                    isPrime[j] = False
                    j += i
            i += 1
        return sum(isPrime)
