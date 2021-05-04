def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for p in range(2, n):
        if n % p == 0:
            return False
    return True
