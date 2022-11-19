import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, idx) -> None:
        self.idx = idx
        self.dests = []
        self.passed = False
    
    def __repr__(self) -> str:
        return f'node:{self.idx}'


def main(n):
    d = defaultdict(list)
    f = defaultdict(bool)
    for _ in range(n):
        a,b = map(int, input().split())
        d[a].append(b)
        d[b].append(a)
    
    if 1 not in d:
        print(1)
        exit()
    
    ans = []
    def dfs(n):
        if not d[n]:
            return
        dests = d[n]
        for _d in dests:
            if f[_d]:
                continue
            ans.append(_d)
            f[_d] = True
            dfs(_d)
    
    dfs(1)
    print(max(ans))

if __name__ == '__main__':
    n = int(input())
    main(n)