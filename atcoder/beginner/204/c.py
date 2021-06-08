import sys
sys.setrecursionlimit(10000)


def main():
    def dfs(v):
        if tmp[v]:  # すでに目的地としてカウントされた都市はスキップ
            return
        tmp[v] = True
        for vv in G[v]:
            dfs(vv)

    N, M = map(int, input().split())
    G = list([] for i in range(N))
    # 通路情報を格納する、どの都市(key)からどの都市(value)に行くことができるか
    for i in range(M):
        A, B = map(int, input().split())
        G[A - 1].append(B - 1)

    ans = 0
    # 1..N個の都市からどこの都市へ行くことができるのかを探索
    for i in range(N):
        tmp = [False] * N  # 目的地になる頂点はTrueとなる
        dfs(i)
        ans += sum(tmp)
    return ans


print(main())
