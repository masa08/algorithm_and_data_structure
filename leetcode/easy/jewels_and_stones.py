class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = list(jewels)
        count = 0

        for stone in list(stones):
            if stone in jewels:
                count += 1

        return count
