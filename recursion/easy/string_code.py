def isMarcusLarger(stringOperand1, stringOperand2):
    sum1 = stringToCodeNumberSum(stringOperand1)
    sum2 = stringToCodeNumberSum(stringOperand2)
    if sum1 > sum2:
        return True

    return False


def stringToCodeNumberSum(string):
    result = 0
    for s in string.lower():
        result += ord(s)
    return result
