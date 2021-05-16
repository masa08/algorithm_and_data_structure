def generateAlphabet(firstAlphabet, secondAlphabet):
    result = []
    first, second = firstAlphabet.lower(), secondAlphabet.lower()
    formerStr = ord(first)
    laterStr = ord(second)
    if formerStr > laterStr:
        formerStr, laterStr = laterStr, formerStr
    for i in range(formerStr, laterStr+1):
        result.append(chr(i))

    return result
