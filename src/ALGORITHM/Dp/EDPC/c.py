_n = lambda: int(_i())
_nl = lambda: list(map(int, _i().split()))
_i = lambda: input()

def run():
    n = _n()
    dp = [[0]*(3) for _ in range(n+1)] # dp[i][j] := i-1 日目に選択肢 j をとったときにとりうる最大の幸福度

    l = []
    for _ in range(n):
        l.append(_nl())

    for i in range(n):
        for j in range(3): # 0: 選択肢 a / 1: 選択肢 b / 2: 選択肢 c
            dp[i+1][j] = max([dp[i][k] + l[i][j] for k in range(3) if j != k]) # 同じ選択肢を 2 日連続でとれないため
    
    print(max(dp[n]))


if __name__ == '__main__':
    run()
