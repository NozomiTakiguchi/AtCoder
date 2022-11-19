from collections import defaultdict
'''
なるべく大きいものから抜いていく
→ 連続している数字は捨てられる
'''

INF = float('inf')
def main(n,m,an):
    d = defaultdict(int)
    for a in an:
        d[a] += 1

    dp= [[INF]*(n+1) for _ in range(n+1)] # dp[i+1][j+1] : i 番目から始め、j 枚抜いた時の残り手札の和の最小

if __name__ == '__main__':
    n,m = map(int, input().split())
    an = list(map(int, input().split()))

    main(n,m,an)
