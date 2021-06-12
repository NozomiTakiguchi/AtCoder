
CAP = (10**9)+10

def gen_cumulative_sum_2d(lim: int, length: int, source: list) -> list:
    """ 渡された数値 (条件) より大きい要素を抽出する (二次元累積和を用いる)

    Args:
        lim (int): 数値 (条件)
        length (int): 判定対象の数値リストの長さ. 二次元累積和リストは n+1 長となる
        source (list): 判定対象の数値リスト

    Returns:
        list: 二次元累積和のリスト
    """    
    cumulative_sum_2d = [[0 for _ in range(length+1)] for __ in range(length+1)]

    for i in range(length):
        for j in range(length):
            cumulative_sum_2d[i+1][j+1] = cumulative_sum_2d[i+1][j] + cumulative_sum_2d[i][j+1] - cumulative_sum_2d[i][j]
            if source[i][j] > lim:
                cumulative_sum_2d[i+1][j+1] += 1

    return cumulative_sum_2d

def run(n, k):
    area = []
    for i in range(n):
        area.append(list(map(int, input().split())))
    
    # 全ての区画の中で、中央値が最も低い区画を抽出する
    # → 「全ての区間の中央値が lim 以上であるか否か」を [0,∞) の区間で調べる
    # → False, False, ... , False , True, True, ..., True というストリームが生成される
    # → この最初の True にあたるところが答え
    # こうやって二分探索を使えるか否かは経験...

    ng = -1
    ok = CAP

    limit = (k*k) // 2 + 1

    while (ng + 1) < ok:
        mid = (ng + ok) // 2 # この値で二分探索する

        s = gen_cumulative_sum_2d(mid, n, area)

        exist = False

        # n*n 区画から k*k 区画は (n-k+1)*(n-k+1) 個作ることができる → これすら最初はわからなかった...
        for i in range(n-k+1):
            for j in range(n-k+1):
                # 問題より、中央値はその区画で lim 番目に高いマスの高さ
                # ある値 x がその区画の中央値であるとき、その区画には高さが x より大きいマスは lim 個未満しかない (当たり前)
                if s[i+k][j+k] + s[i][j] - s[i][j+k] - s[i+k][j] < limit :
                    # ある値 x がこの区画の中央値に `なりうる`
                    exist = True
        if exist:
            ok = mid
        else:
            ng = mid

    print(ok)
    exit()

if __name__ == '__main__':
    n, k = map(int, input().split())
    run(n, k)