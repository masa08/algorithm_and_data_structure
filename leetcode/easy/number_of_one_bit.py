class Solution:
    def hammingWeight(self, n: int) -> int:
        remain = []

        while n != 0:
            remain.append(n % 2)
            n //= 2
        remain.reverse()

        bits = ''.join(map(str, remain))

        result = 0
        for b in bits:
            result += int(b)

        return result

    # def hammingWeight(self, n):
    #     count = 0
    #     bits = str(bin(n))
    #     for b in bits:
    #         if b == '1':
    #             count += 1
    #     return count
