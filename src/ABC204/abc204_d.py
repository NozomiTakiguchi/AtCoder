_n = lambda: int(_i())
_nl = lambda: list(map(int, _i().split()))
_i = lambda: input()

def run():
    n = _n()
    _t = _nl()
    MAX = sum(_t)

    dp = [[False]*(MAX+1) for _ in range(n+1)] # dp[i][j] : インデックス i-1 番目までの料理をいくつか選んで、調理時間を j にできるか
    dp[0][0] = True

    for i in range(n):
        t = _t[i]
        for j in range(MAX+1):
            if dp[i][j]:
                dp[i+1][j] = dp[i][j] # i-1 番目を選んで合計を j にできるから、i 番目を選ばなくても j にできる
            else:
                dp[i+1][j] = False if j - t < 0 else dp[i][j-t] #dp[i][j] が False なので i 番目を使う必要がある

    # x 個料理した 1 台目のほうが長く時間がかかるとすると、 sum(x) >= MAX - sum(x) で合計調理時間は sum(x)
    # sum(x) >= MAX/2 の最小値が答え
    boundary = MAX/2 
    ans = float('inf') 
    for i,j in enumerate(dp[n]):
        if i < boundary:
            continue
        if j:
            ans = min(ans, i)
    
    print(ans)

if __name__ == '__main__':
    run()