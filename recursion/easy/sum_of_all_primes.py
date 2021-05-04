def sumOfAllPrimes(n):
    result = 0
    for i in range(1, n+1):
        if isPrime(i):
            result += i
    return result


def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for p in range(2, n):
        if n % p == 0:
            return False
    return True
