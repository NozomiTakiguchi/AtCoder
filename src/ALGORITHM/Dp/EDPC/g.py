import sys
from collections import deque

class Node:
    def __init__(self, index) -> None:
        self.index = index # 自分の番号 (頂点)
        self.parents = [] # 親ノードのインデックスのリスト
        self.children = [] # 子ノードのインデックスのリスト
        self.toporo = 0
        self.memo = [] # 親ノードのリスト
    
    def __repr__(self) -> str:
        return f'Node {self.index} : toporo {self.toporo} : memo {self.memo}'


# def run(n,m):
def run():
    input = sys.stdin.readline
    n,m = map(int, input().split())

    nodes = []
    for i in range(n+1):
        nodes.append(Node(i))
    
    for _ in range(m):
        s,d = map(int, input().split())
        nodes[s].children.append(d)
        nodes[d].parents.append(s)
        nodes[d].memo.append(s)
    queue = deque()

    # 親ノードを持たない Node をキューに追加 (探索のスタート地点)
    for node in nodes:
        if len(node.parents) == 0:
            queue.append(node)
    
    # トポロジカル順序を初期化
    order = 1

    while queue:
        node = queue.pop() # LIFO で深さ優先する
        nodes[node.index].toporo = order
        order += 1

        children = node.children
        for child in children:
            nodes[child].parents.remove(node.index) # 
        
            if len(nodes[child].parents) == 0:
                queue.append(nodes[child])
    # Node 0 が toporo 順序の最大値 (入力例 1 なら Node 0 が toporo 5 になる) になるので、Node 0 を消す → LIFO だから Node 0 が最後まで残るから order が最大になる
    toporo_nodes = sorted(nodes, key=lambda x: x.toporo)[: -1]

    print(f'toporo: {toporo_nodes}')

    # dp[i+1]:  トポロジカル順序 i の Node まで調べた時、その Node を徹最長経路
    dp = [0] * (n)
    for i in range(1, n):
        if len(toporo_nodes[i].memo) > 0:
            dp[i] = max([dp[j-1] for j in [nodes[k].toporo for k in toporo_nodes[i].memo]]) + 1
    
    print(max(dp))


if __name__ == '__main__':
    # n,m = map(int, input().split())
    # run(n,m)
    run()

