import time
import numpy as np
def run(n, c, _list):
    '''
    いもす法でできるか思ったが i のイベント日の範囲がかなり大きいのでそのままでは無理 
    '''
    # _m = sorted(_list, key=lambda e: e[1], reverse=True)[0][1]
    # _s = sorted(_list, key=lambda e: e[0])[0][0]
    # _l = [0]*(_m+10 - _s)

    # max_date = 0
    # for i in range(n):
    #     s_date = _list[i][0]
    #     e_date = _list[i][1]
    #     cost = _list[i][2]

    #     max_date = e_date if max_date <= e_date else max_date

    #     _l[s_date-1] += cost
    #     _l[e_date] -= cost

    
    # # for i in range(max_date + 10):
    # for i in range(len(_l) - 1):
    #     _l[i+1] += _l[i]

    #     if _l[i] > c:
    #         _l[i] = c

    # print(sum(_l))

    _l = []
    for i in range(n):
        s_date = _list[i][0]
        e_date = _list[i][1]
        cost = _list[i][2]

        _l.append((s_date -1, cost))
        _l.append((e_date, -cost))
    
    _l.sort()
    print(_l)
    ans = 0
    fee = 0
    t = 0
    for x, y in _l:
        if x != t:
            ans += min(c, fee)*(x - t)
            print(ans)
            t = x
        fee += y
    
    print(ans)






if __name__ == '__main__':
    n, c = map(int, input().split())
    _list = [list(map(int, input().split())) for _ in range(n)]

    run(n, c, _list)