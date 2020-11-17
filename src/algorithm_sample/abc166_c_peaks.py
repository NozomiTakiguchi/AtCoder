'''
方針 -> 道毎にループ. 両展望台の高さを比べて、小さいほうを False. 一度 False になったら検査の対象外にする
結果 -> 50 分くらいかかった... 模範解答は、展望台毎にループして高さの最大値をとっている感じ
'''
def run(n, m, h, ab):
    hights = [True]*n

    # 要素は tuple
    for roads in ab:

        # 展望台の情報
        left = roads[0]
        right = roads[1]

        # 高さの情報
        hight_left = h[left - 1]
        hight_right = h[right - 1]
        # print('observatory_left=[{}] (hight=[{}]) / observatory_right=[{}] (hight=[{}])'.format(left, hight_left, right, hight_right))

        if hight_left == hight_right:
            hights[left - 1] = False
            hights[right - 1] = False
            continue

        # すでに False だったら「良い展望台」にはなりえないので False. あるいは、小さかったら False
        hights[left - 1] = False if not hights[left - 1] or hight_left < hight_right else True
        hights[right - 1] = False if not hights[right - 1] or hight_right < hight_left else True
        continue

    print(len([e for e in hights if e]))

if __name__ == '__main__':
    # 展望台, 道 の数
    n, m = map(int, input().split())
    # 展望台のそれぞれの高さ
    h = list(map(int, input().split()))
    # 道
    ab = [tuple(map(int, input().split())) for _ in range(m)]
    run(n, m, h, ab)