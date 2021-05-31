# input = list(map(int, input().split()))
# n, k = input
# result = 0
# for i in range(1, n+1):
#     for j in range(1, k+1):
#         roomNumber = i * 100 + j
#         result += roomNumber
# print(result)

n, k = list(map(int, input().split()))
ans = 0
for i in range(1, n+1):
    for j in range(1, k+1):
        ans += 100*i+j
print(ans)
