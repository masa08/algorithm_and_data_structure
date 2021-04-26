# recursion
def numberOfDots(x):
    def _numberOfDots(x, res):
        if x == 1:
            return res + 1
        res += x
        x -= 1

        return _numberOfDots(x, res)

    return _numberOfDots(x, 0)

# iteration
# def numberOfDots(x):
#     result = calc(x)
#     return result

# def calc(x):
#     num = 0
#     while x:
#         num += x
#         x -= 1
#     return num
