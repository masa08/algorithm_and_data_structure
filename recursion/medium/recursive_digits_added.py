def recursiveDigitsAdded(digits):
    def _recursiveDigitsAdded(digits, result):
        sumNumber = splitAndAdd(digits)
        result += sumNumber
        if sumNumber < 10:
            return result
        return _recursiveDigitsAdded(sumNumber, result)

    return _recursiveDigitsAdded(digits, 0)


def splitAndAdd(digits):
    result = 0
    string = str(digits)
    strings = list(string)

    for s in strings:
        result += int(s)

    return result
