def decimalToHexadecimal(decNumber):
    remain = []
    val = [i for i in range(0, 17)]
    letters = list("0123456789ABCDEF")
    d = dict(zip(val, letters))

    while decNumber != 0:
        remain.append(d[decNumber % 16])
        decNumber //= 16

    remain.reverse()
    return ''.join(map(str, remain))
