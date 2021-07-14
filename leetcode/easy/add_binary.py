class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ad = binaryToDecimal(a)
        bd = binaryToDecimal(b)
        decimal = int(ad) + int(bd)

        return decimalToBinary(decimal)


def binaryToDecimal(decNumber: str) -> str:
    remain = 0
    mod = 1
    for i in decNumber[::-1]:
        cal = int(i) * mod
        remain += cal
        mod *= 2

    return str(remain)


def decimalToBinary(decNumber: int) -> str:
    if decNumber == 0:
        return "0"
    remain = []
    while decNumber != 0:
        remain.append(decNumber % 2)
        decNumber //= 2
    remain.reverse()

    return ''.join(map(str, remain))
