_n = lambda: int(_i())
_l = lambda: list(map(int, _i().split()))
_i = lambda: input()

INF = float('inf')

# 3/34 が WA になり AC しない。。
def run():
    h,w,c = _l()
    _a = []

    for _ in range(h):
        _a.append(_l())
    
    dp = [[INF] * (w+1) for _ in range(h+1)] #駅を建設して (i,j) にいるときに、それまでにかかった費用の最小値
    x = [[INF] * (w+1) for _ in range(h+1)] # 2 つめの駅を (i,j) に建設したときに、それまでにかかった費用の最小値
    
    for i in range(h):
        for j in range(w):
            a = _a[i][j]
            # (i,j) に駅を建設する場合 or
            # あるところに駅を建設し、線路を引きながら (i,j) に移動してきた場合
            dp[i+1][j+1] = min(a, dp[i][j+1]+c, dp[i+1][j]+c)
            x[i+1][j+1] = min(dp[i+1][j]+c+a, dp[i][j+1]+c+a)
    
    ans = INF
    for i in range(h):
        for j in range(w):
            ans = min(ans, x[i+1][j+1])

    print(ans)

if __name__ == '__main__':
    run()