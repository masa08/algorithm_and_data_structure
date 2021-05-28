import math


def shuffleSuccessRate(arr, shuffledArr):
    movedCount = 0
    for i, a in enumerate(arr):
        index = shuffledArr.index(a)
        if i != index:
            movedCount += 1

    return math.floor(movedCount / len(arr) * 100)
