import itertools
import math
def run(n, xy):
    '''

    '''
    _list = [(x, y) for x,y in xy]

    # 組み合わせを取得
    for elm in list(itertools.combinations(_list, 3)):
        first, second, third = elm

        # x = a の直線の場合
        if second[0] - first[0] == 0:
            if second[0] == third[0]:
                print('Yes')
                break
        elif ((second[1] - first[1])/(second[0] - first[0]))*(third[0] - first[0]) + first[1] == third[1]:
            print('Yes')
            break
    else:
        print('No')
    
    # A(x1, y1) が原点になるように平行移動したのち、 AB の傾き = AC の傾き となるかどうかを判定する (↓ 模範解答)

    # for i in range(n):
    #     for j in range(i):
    #         for k in range(j):
    #             x1, y1 = xy[i]
    #             x2, y2 = xy[j]
    #             x3, y3 = xy[k]
    #             x1 -= x3
    #             x2 -= x3
    #             y1 -= y3
    #             y2 -= y3
    #             if x1 * y2 == x2 * y1:
    #                 print("Yes")
    #                 exit()
    # print('No')



if __name__ == '__main__':
    n = int(input())

    # map 関数は iteretor を返すため、内容を確認したいときは ↓ みたいに tuple() や list() で囲んであげる必要がある
    # 今回の問題は 2 値複数行のインプットなので、 tuple で囲んであげるのが良い (↓ は模範解答)
    # xy = [tuple(map(int, input().split())) for i in range(n)]

    xy = list(map(int, input().split()) for _ in range(n))

    run(n, xy)