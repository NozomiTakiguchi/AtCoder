_n = lambda: int(_i())
_l = lambda: list(map(int, _i().split()))
_i = lambda: input()

MOD = 10**9+7
def run():
    n = _n()
    _a = _l()
    dp = [[0]*2 for _ in range(n+1)] # dp[i][j] := i-1 番目に符号 j を入れた時の数列の和
    for i in range(2):
        dp[1][i] = _a[0]

    x,y = 1,1
    for i in range(1,n):
        a = _a[i]
        # for j in range(2): # 0: + / 1: -
        #     if i-1 <= 0:
        #         dp[i+1][j] = dp[i][j] + [a, -a][j]
        #     else:
        #         dp[i+1][j] = sum([dp[i][k] for k in range(2)] if j == 0 else [dp[i][0]-a])
        #         dp[i+1][j] += (pos if j == 0 else neg)*[a, -a][j]
        #         pos,neg = pos+neg,pos

    
    print(sum(dp[n])%MOD)


        


if __name__ == '__main__':
    run()