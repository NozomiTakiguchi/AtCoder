_n = lambda: int(_i())
_nl = lambda: list(map(int, _i().split()))
_i = lambda: input()

'''
d と問題は同じだが、制約条件が違う
w の最大値が 10**9 のため、リストが作れない
'''

V = (10**2)*(10**3)
INF = float('inf')

def run():
    n,w = _nl()
    _l = [_nl() for _ in range(n)]

    # dp = [[0]*(w+1) for _ in range(n+1)] #dp[i][j] := i-1 番目までの品物から重さが j を超えないようにいくつか選んだ時の価値の総和の最大
    dp = [[INF]*(V+1) for _ in range(n+1)] #dp[i][j] := i-1 番目までの品物から価値が j となるようにいくつか選んだ時の重さの最小
    dp[0][0] = 0

    for i in range(n):
        _w,v = _l[i]
        for j in range(V+1): #dp[0][j] は品物を一つも選ばないときの結果なので答えになりうる値は dp[1][j] 以降
            dp[i+1][j] = dp[i][j] if j-v < 0 else min(dp[i][j], dp[i][j-v] + _w)
    
    ans = 0
    for i,_w in enumerate(dp[n]): # i は価値、_w は重さ
        # if _w != INF:
        #     print(_w, i)
        if _w <= w:
            ans = max(ans,i)

    print(ans)

if __name__ == '__main__':
    run()