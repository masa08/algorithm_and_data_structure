
def main():
    pattern = [0, 1, 2]
    a, b = map(int, input().split())
    if a == b:
        return a
    else:
        pattern.remove(a)
        pattern.remove(b)
        return pattern[0]


print(main())
