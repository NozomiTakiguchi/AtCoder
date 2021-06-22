
ni = lambda: int(_n())
na = lambda: list(map(int, input().split()))
_n = lambda: input()

def max_sum(n:int, a:list):
    '''
    dp[i+1] := i 番目までの整数の中からいくつか選んで総和をとったときの、総和の最大値
    dp[0] := 何も選ばない状態
    dp[1] := 0 番目の数字だけ選んだ状態
    '''
    dp = [0]*(n+1)
    for i in range(n):
        dp[i+1] = max(dp[i], dp[i]+a[i])
    
    return dp[n]


def run():
    n = ni()
    a = na()

    ans = max_sum(n, a)
    print(ans)

if __name__ == '__main__':
    run()