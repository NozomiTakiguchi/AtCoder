import sys
sys.setrecursionlimit(10**8)

class Node:
    def __init__(self, idx) -> None:
        self.idx = idx
        self.children = []
        self.parents = []
        self.order = 0

    def __repr__(self) -> str:
        return f'Node:{self.idx}, child:{self.children}, parents:{self.parents}, order:{self.order}'

n = int(input())
a = list(map(int, input().split()))

nodes = []
for i in range(2*max(a)+1+1):
    nodes.append(Node(i))

nodes[1].parents.append(0)
for i,_a in enumerate(a):
    node = nodes[_a]
    child1 = (i+1)*2
    child2 = (i+1)*2 + 1

    node.children.append(child1)
    node.children.append(child2)

    child1_node = nodes[child1]
    child1_node.parents.append(_a)
    child2_node = nodes[child2]
    child2_node.parents.append(_a)

def dfs(n,idx):
    node = nodes[n]
    if len(node.parents) == 0:
        return
    node.order = idx
    for child in node.children:
        dfs(child, idx+1)

dfs(1,0)

print(nodes[1].order)
for i in a:
    node = nodes[i]
    for child in node.children:
        print(nodes[child].order)