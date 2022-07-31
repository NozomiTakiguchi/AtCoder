from collections import deque

'''
トポロジカルソートの本質
 * 探索のスタート地点を把握する → 親ノードがいないノード = 自身が親になりうるノード が探索のスタート地点
 * 探索地点のノードの子ノードを把握する → 自分以外に親ノードがいる場合、そちらの探索が終わるまでその子ノードはトポロジカルソートされない。他に親ノードがいない場合、次の探索ターゲットとなる
 * 探索は深さ優先で行う → deque/queue で pop する
'''
class Node:
    def __init__(self, index) -> None:
        self.index = index
        self.topolo_order = 0
        self.children = []
        self.parents = []
        self.parents_cache = []
    
    def __repr__(self) -> str:
        return f'Node:{self.index} With Parents:{self.parents_cache}/Topolo:{self.topolo_order}'

def run(n,m,xy):
    nodes = []
    for i in range(n+1):
        nodes.append(Node(i)) # Node[0] は使わない
    
    for e in xy:
        nodes[e[0]].children.append(e[1])
        nodes[e[1]].parents.append(e[0])
        nodes[e[1]].parents_cache.append(e[0])
    
    queue = deque()
    for node in nodes:
        if len(node.parents) == 0:
            queue.append(node) # 親がいない node を探索の最初スタート地点にする. ↓ の queue.append とは意味が違う
    
    topolo_order = 1
    while queue:
        node = queue.pop() # リストは参照なので、ここで node に変更加えれば list の node にも反映される
        node.topolo_order = topolo_order
        topolo_order += 1

        for child in node.children:
            nodes[child].parents.remove(node.index)

            if len(nodes[child].parents) == 0:
                queue.append(nodes[child])
    topolo_nodes = sorted(nodes, key=lambda node: node.topolo_order)[:-1] # Node0 を削除

    dp = [0]*(n+1) # dp[i+1]: トポロジカル順序 i まで到達したときの、その node までの最長経路
    for i in range(n):
        # 親がいたらカウントが 1 ずつ増えるイメージ
        for k in topolo_nodes[i].parents_cache: # (一つ以上の) 親ノードまでの topolo_order の内最大値を得る. 独立したノードは parents_cache 0 なのでループに入らない
            dp[i+1] = max(dp[i+1], dp[nodes[k].topolo_order]+1)
    
    print(max(dp))


if __name__ == '__main__':
    n,m = map(int, input().split())
    xy = [list(map(int, input().split())) for _ in range(m)]
    run(n,m,xy)