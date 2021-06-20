
import sys
sys.setrecursionlimit(200010)

_i = lambda: map(int, input().split())
p = lambda: list(map(int, input().split()))


# https://qiita.com/DancingEnginee1/items/957e536e5f076e98d5ec
class UnionFind():
    def __init__(self, n):
        self.parent = [-1 for _ in range(n)]
        # 正 : 子要素である & 根の頂点の番号が入る
        # 負 : 親要素である & 連結頂点数が入る (size)
        # 一つのリストに複数の意味がこめられているのでわかりづらいなぁ

    def is_root(self, x):
        return self.parent[x] < 0

    def find(self, x):
        """自分の根を返す.
           自分自身が根の時は自分を返す

        Args:
            x int: 自分自身

        Returns:
            [int]: 根
        """
        if self.is_root(x):
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def size(self, x):
        """自分と連結する頂点の数を返す

        Args:
            x (int): 自分自身. 根である前提

        Returns:
            [int]: 頂点数
        """
        x = self.find(x)
        return -1 * self.parent[x]

    def unite(self, x, y):
        """ 根が異なる二つの木を結合する
            ここではスワップしたい二つの要素が属する木を結合する(ABC097)

        Args:
            x (int): 要素 
            y (int): 要素
        """

        # それぞれの根を取得する
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        else:
            # どっちでもいいが、ここでは大きい木構造にマージして根を更新する
            if self.size(rx) < self.size(ry):
                rx,ry = ry,rx
            
            # 大きいほうの木構造の頂点数を更新
            self.parent[rx] += self.parent[ry]

            # 小さいほうの根を大きいほうの根に更新している
            self.parent[ry] = rx

    def equiv(self, x, y):
        """渡された二つの要素が同じ気に属するかを判定する

        Args:
            x (int): 要素
            y (int): 要素

        Returns:
            [bool]: 同じ木構造に属するなら True
        """
        return self.find(x) == self.find(y)

def run():
    n,m = _i()
    pn = p()

    cnt = 0

    uf = UnionFind(n)

    for i in range(m):
        p1, p2 = _i()
        # インデックスを渡したいのでそれぞれ -1 
        # 経路圧縮 (根を繋ぎ変えることで木構造をフラットに保つ) して根を更新
        uf.unite(p1-1, p2-1)

    for i in range(n):
        uf.find(i)
    
    for i in range(n):
        if pn[i] == i+1:
            cnt += 1
        else:
            # ↓ コメントアウトしているやり方でもイケるが直観的でない
            # if uf.equiv(pn[i]-1, pn[pn[i]-1]-1):
            if uf.equiv(i, pn[i]-1):
                cnt += 1
            else:
                continue
    # print(uf.parent)
    print(cnt)

if __name__ == '__main__':
    '''
    多分考え方としては
     * スワップできる整数のペアを取得する
     * スワップできるペアが例えば (1,3), (2,4), (3,5) だとすると、 (1,3,5) の数値は自由にスワップできる
     * ので、これらのグループを木構造で捉える
     * UnionFind を考える
     みたいな感じ
    '''
    run()