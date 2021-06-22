
na = lambda: list(_nm())
_nm = lambda: map(int, _i().split())
_i = lambda: input()

def knapsack(n: int, w: int, weight_value_pair: list):
    """ dp[i+1][w] := i 番目までの品物から重さの総量が w を超えないようにいくつか選んだ時の、価値の総和の最大値

    Args:
        n (int): 選ぶ個数
        w (int): 上限
        weight_value_pair (list): (weight, value) の set を要素に持つリスト
    
    Returns:
        dp[n][w] (int): 最大値
    """
    INF = float('inf') #正の無限大
    dp = [[-INF for _ in range(w+1)] for _ in range(n+1)]
    for i in range(w+1):
        dp[0][i] = 0
    
    for i in range(n):
        weight, value = weight_value_pair[i]

        # 重量 0 <= j <= w ごとに、価値の最大値を求める
        for j in range(w+1):
            if weight <= j:
                dp[i+1][j] = max(dp[i][j - weight] + value, dp[i][j])
            else:
                dp[i+1][j] = dp[i][j]
    
    return dp[n][w]
            
def run():
    n, w = _nm()
    _l = [na() for _ in range(n)]

    ans = knapsack(n, w, _l)

    print(ans)

if __name__ == '__main__':
    run()