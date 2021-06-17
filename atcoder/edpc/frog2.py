def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    DP = [0]*N

    for i in range(1, N):
        cnt = []
        # iまで判定、始点はi-kがあればそこから
        for j in range(max(i-K, 0), i):
            # 各踏み場からのコストをcntに格納
            cnt.append(abs(h[i]-h[j])+DP[j])
        # 最小値を代入
        DP[i] = min(cnt)

    return DP[N-1]


print(main())
