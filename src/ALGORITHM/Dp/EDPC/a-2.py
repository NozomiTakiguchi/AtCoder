'''
4
10 30 40 20
1->2->4 と移動すれば、最小の移動コスト |10-30|+|30-20|=30 となる
'''
def run(n,h):
    dp = [0]*(n) # 足場1 にいるときはコストゼロ

    for i in range(1,n):
        if i < 2:
            dp[i] = dp[i-1] + abs(h[i-1]-h[i])
        else:
            dp[i] = min(dp[i-1] + abs(h[i-1]-h[i]), dp[i-2] + abs(h[i-2] - h[i]))
    
    print(dp[n-1])

if __name__ == '__main__':
    n = int(input())
    h = list(map(int, input().split()))

    run(n,h)