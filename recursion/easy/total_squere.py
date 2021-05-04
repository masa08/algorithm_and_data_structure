def totalSquareArea(x):
    if x == 0:
        return 0

    return x**3 + totalSquareArea(x-1)
