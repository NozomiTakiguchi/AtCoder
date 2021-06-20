import sys
sys.setrecursionlimit(500005)

ni = lambda: int(_n()) # ni はまだ評価されていないので、 _n をここより下に定義しても大丈夫
na = lambda: list(map(int, input().split()))
_n = lambda: input()

upper = [-1] * 200001

def root(x: int):
    """Union Find 木の根を取得する.
       解決した値にさらに上位要素が存在する可能性を考慮する(親の親の....の親が根、みたいな)

    Args:
        x (int): 要素

    Returns:
        int : 要素の根
    """
    if upper[x] < 0:
        # 真に x の根である
        return x
    else:
        # さらに上位の要素がないかを検索する
        upper[x] = root(upper[x])
        return upper[x]

# 参考にしたプログラムから↓の通りコメントアウトしても AC にはなる
def unite(x,y):
    rx,ry = root(x), root(y)
    if rx != ry:
        # ↓の意図がよくわかっていない
        # if upper[ry] < upper[rx]:
        #     rx,ry = ry,rx #入れ替える
        # upper[rx] += upper[ry] # これやる意味ある？
        # ↑ ここまで
        upper[ry] = rx
    return rx == ry


def run():
    n = ni()
    a = na()
    con = 0
    for i in range(n):
        # ここは while 使って i をインクリメントする方が効率的かも
        if i < n-1-i:
            if not unite(a[i], a[n-1-i]):
                con += 1
    print(con)

if __name__ == '__main__':
    run()
