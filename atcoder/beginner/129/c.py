# N, M = map(int, input().split())
# A = set([int(input()) for _ in range(M)])
# mod = 10**9+7
# dp = [0]*(N+1)
# dp[0] = 1
# for i in range(1, N+1):
#     if i in A:
#         continue
#     dp[i] = (dp[i-1]+dp[i-2]) % mod
# print(dp[N])

N, M = map(int, input().split())
A = set([int(input()) for _ in range(M)])
mod = 10**9+7

dp = [0]*(N+1)
dp[0] = 1
if not 1 in A:
    dp[1] = 1
for i in range(2, N+1):
    if i in A:
        continue
    dp[i] = (dp[i-1] + dp[i-2]) % mod
print(dp[N])
