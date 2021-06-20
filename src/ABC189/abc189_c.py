import numpy as np
def run(n, _l):
    '''

    '''
    ans = 0
    before = 0

    for i,e in enumerate(_l):
        if ans == 0:
            ans = e
        elif before != e:
            if before < e:
                ans = e if e > ans + before else ans + before
            else:
                _l_sliced = _l[:i+1]
                _amount = e*len([m for m in _l_sliced if m >= e])
                # ans = ans if ans > e*(i+1) else e*(i+1)
                print(e,_amount)
                ans = ans if ans > _amount else _amount
        
        print(ans)
        before = e

    print(ans)

if __name__ == '__main__':
    n = int(input())
    _l = list(map(int, input().split()))

    run(n, _l)