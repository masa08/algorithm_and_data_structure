from collections import deque

def minWindowArrK(intArr,k):
    if k > len(intArr): return []
    results = []
    d = deque()

    # dを初期化(k番目まで)、先頭に最小値がくる
    for i,num in enumerate(intArr[:k]):
        while len(d) > 0 and intArr[d[-1]] >= num: d.pop()
        d.append(i)

    # k+1番目以降の精査
    for i,num in enumerate(intArr[k:],k):
        results.append(intArr[d[0]])
        # i..i+kの範囲に入らないindexを除外する
        while len(d) > 0 and d[0] <= i-k: d.popleft()
        while len(d) > 0 and intArr[d[-1]] >= num: d.pop()
        d.append(i)
    results.append(intArr[d[0]])

    return results
