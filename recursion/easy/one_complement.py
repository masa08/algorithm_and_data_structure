def oneComplement(bits):
    result = []
    for i in range(len(bits)):
        if bits[i] == '0':
            result.append('1')
        else:
            result.append('0')
    return ''.join(result)
