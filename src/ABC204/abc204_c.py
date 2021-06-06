import sys

# 再帰の最大回数を増やしておくことで、 AC になるパターンが多いらしい
# 再帰の回数をデフォルトのまま (1000) にしておくと Runtime Error(Stack Over Flow) になることがあるらしい
sys.setrecursionlimit(10000)

def dfs(start_point: int, mapping: list, _result: list, avoid_duplicate=True):
    """ 深さ優先探索アルゴリズム

    Args:
        start_point (int): 経路を検証したい頂点. 
        mapping (list): 頂点と,その隣接する頂点のリスト. それぞれインデックスを要素として入れる (頂点 2 と隣接する頂点が 4 のとき、リストには [[..], [3], [..],[..]] とする)
        _result (list): 初期値は [False] * 頂点数のリスト. 再帰的に参照する.
        avoid_duplicate (bool, optional): 同じ頂点を二度以上調べたい場合は False. たぶん False にすることはない.
    """
    if _result[start_point]:
        if avoid_duplicate:
            return 

    # 自分自身と繋がっている
    _result[start_point] = True
    for v in mapping[start_point]: # 渡された頂点と隣接する頂点に関して調べる
        dfs(v, mapping, _result)

def run(n, m):
    _l = [[] for _ in range(n)]
    # _l[i] は、都市 i+1 から道路で直接つながっている都市の「インデックス」のリスト 
    for _ in range(m):
        a, b = map(int, input().split())
        _l[a-1].append(b-1)

    ans = 0
    for i in range(n):
        result = [False]*n
        dfs(i, _l, result)
        # print(f'mapping is {_l}')
        # print(f'city {i+1} is connected to {result}')
        ans += sum(result)
    print(ans)


if __name__ == '__main__':
    n, m = map(int, input().split())
    run(n, m)