# input = list(map(int, input().split()))
# a, b, c = input
# numberList = set(input)

# if len(numberList) == 1:
#     print(a)
# elif len(numberList) == 3:
#     print(0)
# else:
#     if input.count(a) == 1:
#         print(a)
#     if input.count(b) == 1:
#         print(b)
#     if input.count(c) == 1:
#         print(c)

a, b, c = map(int, input().split())
if a == b:
    print(c)
elif b == c:
    print(a)
elif c == a:
    print(b)
else:
    print(0)
