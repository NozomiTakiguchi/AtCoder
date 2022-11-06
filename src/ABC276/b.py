class Node:
    def __init__(self, idx) -> None:
        self.idx = idx
        self.dest = []
    
    def __repr__(self) -> str:
        return f'node:{self.idx}. dest:{self.dest}'
    
n,m = map(int, input().split())

nodes = []
for i in range(n+1):
    nodes.append(Node(i))

for _ in range(m):
    a,b = map(int, input().split())
    nodes[a].dest.append(b)
    nodes[b].dest.append(a)

for i in range(n):
    node = nodes[i+1]
    ans = node.dest

    _len = len(node.dest)
    if _len == 0:
        print(0)
    else:
        ans = sorted(ans)
        print(_len, *ans)