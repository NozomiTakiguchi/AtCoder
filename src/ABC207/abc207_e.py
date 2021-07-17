'''
動的計画法の練習問題
https://algo-logic.info/tree-dp/
https://atcoder.jp/contests/abc207/submissions/23743953
'''

_n = lambda: int(_i())
_nl = lambda: list(map(int, _i().split()))
_i = lambda: input()

MOD = (10**9)+7

def run():
    n = _n()
    a = _nl()

    dp = [[0]*(n+1) for _ in range(n+1)] # dp[i][j] : 先頭からインデックス i-1 番目の数までで条件に合うように j 組作ったときの組み合わせ？

if __name__ == '__main__':
    run()
