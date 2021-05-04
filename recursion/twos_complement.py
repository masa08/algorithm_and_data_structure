def twosComplement(bits):
    oneComplements = oneComplement(bits)
    twoComplements = ""

    for i in range(len(oneComplements)-1, -1, -1):
        if oneComplements[i] == "0":
            return oneComplements[0:i] + "1" + twoComplements
        else:
            twoComplements = "0" + twoComplements

    return "1" + twoComplements


def oneComplement(bits):
    result = []
    for i in range(len(bits)):
        if bits[i] == '0':
            result.append('1')
        else:
            result.append('0')
    return ''.join(result)
