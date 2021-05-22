def addEveryOtherElement(intArr):
    result = 0

    for i in range(len(intArr)):
        if i % 2 == 0:
            result += intArr[i]
            print(result)

    return result
