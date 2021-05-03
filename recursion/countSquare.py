def countSquare(x, y):
    gcdNumber = gcd(x, y)
    return (x*y) // (gcdNumber**2)


def gcd(m, n):
    if m == n:
        return m
    elif m > n:
        return gcd(m-n, n)
    else:
        return gcd(m, n-m)
