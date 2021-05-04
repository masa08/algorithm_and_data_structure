def decimalToBinary(decNumber):
    remain = []

    while decNumber != 0:
        remain.append(decNumber % 2)
        decNumber //= 2
    remain.reverse()

    return ''.join(map(str, remain))
