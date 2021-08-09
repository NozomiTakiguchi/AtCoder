_n = lambda: int(_i())
_l = lambda: list(map(int, _i().split()))
_i = lambda: input()

import sys
sys.setrecursionlimit(300000)

ans = []
def dfs(crr: int, pre: int, l:list):
    ans.append(crr)
    for nxt in l[crr]:
        if nxt != pre:
            dfs(nxt, crr, l)
            ans.append(crr)

def run():
    n = _n()
    l = [[] for _ in range(n+1)]

    for i in range(n-1):
        a,b = _l()
        l[a].append(b)
        l[b].append(a)
    
    for i in range(n+1):
        l[i].sort()
    
    dfs(1,-1, l)

    print(*ans)


if __name__ == '__main__':
    run()