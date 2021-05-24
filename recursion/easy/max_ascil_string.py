def maxAscilString(stringList):
    maxValue = 0
    maxIndex = 0
    for i, s in enumerate(stringList):
        targetValue = 0
        for c in s:
            targetValue += ord(c.lower())
        if targetValue > maxValue:
            maxValue = targetValue
            maxIndex = i

    return maxIndex
