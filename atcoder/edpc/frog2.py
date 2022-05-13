# input example
# 5 3
# 10 30 40 50 20


def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))

    # init list for dp
    DP = list(0 for _ in range(N))

    # fix first and secound cost
    DP[0] = 0
    DP[1] = abs(h[1]-h[0])

    for i in range(2, N):
        cnt = []
        for j in range(max(i-K, 0), i): # iまでのコスト判定、始点はi-kがあればそこから
            cnt.append(abs(h[i]-h[j])+DP[j]) # 各踏み場からのコストをcntに格納
        DP[i] = min(cnt) # 最小値を代入

    return DP[-1]


print(main())
