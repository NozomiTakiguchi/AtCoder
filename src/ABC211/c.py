from collections import defaultdict

_n = lambda: int(_i())
_l = lambda: list(map(int, _i().split()))
_i = lambda: input()

CHOKUDAI = ['c','h','o','k','u','d','a','i']
MOD = 10**9+7
# def run():
#     s = _i()

#     dic = defaultdict(int)
#     for e in s:
#         if e not in CHOKUDAI:
#             continue
#         if e == 'c':
#             dic[e] += 1
#         elif e == 'h':
#             dic[e] += dic['c']
#         elif e == 'o':
#             dic[e] += dic['h']
#         elif e == 'k':
#             dic[e] += dic['o']
#         elif e == 'u':
#             dic[e] += dic['k']
#         elif e == 'd':
#             dic[e] += dic['u']
#         elif e == 'a':
#             dic[e] += dic['d']
#         elif e == 'i':
#             dic[e] += dic['a']
    
#     print(dic[('i')]%MOD)

def run():
    s = _i()
    t = 'chokudai'
    dp = [[0]*9 for _ in range(len(s)+1)] # dp[i][j] : i-1 文字目までを使って、 t の j-1 文字目までを選択する方法
    dp[0][0] = 1
    for i in range(len(s)):
        for j in range(8):
            dp[i+1][j+1] = dp[i][j+1] if s[i] != t[j] else dp[i][j+1] + dp[i][j]





if __name__ == '__main__':
    run()
