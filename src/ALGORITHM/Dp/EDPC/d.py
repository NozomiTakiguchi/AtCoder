_n = lambda: int(_i())
_nl = lambda: list(map(int, _i().split()))
_i = lambda: input()

def run():
    n,w = _nl()
    l = [_nl() for _ in range(n)]

    dp = [[0]*(w+1) for _ in range(n+1)] #dp[i][j] := i-1 番目までの品物から j を超えないようにいくつか選んだ時の価値の総和の最大

    for i in range(n):
        for j in range(w+1): #インデックスがよくわからない
            _w,v = l[i]
            dp[i+1][j] = dp[i][j] if j-_w<0 else max(dp[i][j], dp[i][j-_w] + v)
    
    print(max(dp[n]))


if __name__ == '__main__':
    run()