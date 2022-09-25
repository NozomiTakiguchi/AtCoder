# Pypy じゃなくて Python3.8.2 にしたら AC した。。。
import sys
sys.setrecursionlimit(10**9)
 

class Node:
    def __init__(self, idx) -> None:
        self.idx = idx
        self.checked = False
        self.dests = []
 

def run(n,x,y,uv):
    nodes = []
    for i in range(n+1):
        nodes.append(Node(i))
    
    for e in uv:
        nodes[e[0]].dests.append(e[1])
        nodes[e[1]].dests.append(e[0])
    
    n = nodes[x]

    # dfs すると TLE 数問と WA 数問、、、 WA に関しては何でかよくわからん
    # → parents と children みたいにしてたからおかしくなってたっぽい... TLE は変わらんけど WA はなくなった
    if dfs(nodes, y, n):
        ans.append(x)
    ans.reverse()
 
    # print(' '.join(map(str, ans)))
    print(*ans)


ans = []
def dfs(nodes, y, node):
    node.checked = True
    if y in node.dests:
        ans.append(y)
        return True
    
    for d in node.dests:
        node = nodes[d]
        if node.checked:
            continue
        if dfs(nodes, y, node):
            ans.append(node.idx)
            return True


if __name__ == '__main__':
    n,x,y = map(int, input().split())
    uv = [list(map(int, input().split())) for _ in range(n-1)]
    run(n,x,y,uv)