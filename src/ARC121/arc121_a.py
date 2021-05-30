import itertools

def run(n, _l):
    '''
    全探索すると圧倒的に TLE になるため、条件に合致する要素をどうやって数式で表せるかを考える
    チェビシェフ距離 (max(|xi - xj|, |yi - yj|)) の降順で 2 番目に遠い家の組み合わせの、その距離を求める問題なので
    どんな組み合わせと 2 番目に遠くなるかを考える
    '''
    _x = sorted(_l, key=lambda x: x[0]) # x の座標の昇順で並べ替え
    # 同じ座標に家が複数存在する場合があり、x の要素の中では重複を許容する
    x_candidate_list = [_x[0], _x[1], _x[-2], _x[-1]] # _x[0] <-> _x[-2] or _x[1] <-> _x[-1] が 2 番目に遠い距離になりうる家の組み合わせ

    # y も同様
    _y = sorted(_l, key=lambda x: x[1])
    y_candidate_list = [_y[0], _y[1], _y[-2], _y[-1]]


    # e.g. [0, 0], [0, 0], [1, 0], [1, 1] の場合は candidate = [[0, 0], [0, 0], [1, 0], [1, 1]] となるようにしたい.
    # ↓ は [[0, 0], [1, 0], [1, 1]] になってしまう
    # candidate_list = x_candidate_list + y_candidate_list
    # candidate = []
    # for e in candidate_list:
    #     if e in candidate:
    #         continue
    #     candidate.append(e)


    # ↑ では同じ座標の違う家を認識できなかったので、↓ では x_candidate_list をベースに y の要素を足すようにしたらうまくいった
    candidate = x_candidate_list
    for e in y_candidate_list:
        if e in candidate:
            continue
        candidate.append(e)

    distance = []
    for elm in itertools.combinations(candidate, 2):
        e1 = elm[0]
        e2 = elm[1]
        distance.append(max([abs(e1[0]-e2[0]), abs(e1[1]-e2[1])]))

    distance.sort()
    print(distance[-2])

if __name__ == '__main__':
    n = int(input())
    _l = [list(map(int, input().split())) for _ in range(n)]

    run(n,_l)