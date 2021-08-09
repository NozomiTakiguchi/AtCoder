from collections import defaultdict
_n = lambda: int(_i())
_l = lambda: list(map(int, _i().split()))
_i = lambda: input()

def run():
    h,w,n = _l()
    l = []

    x,y = [], []
    for _ in range(n):
        a,b = _l()
        x.append(a)
        y.append(b)
    
    # 座業圧縮する. x 軸と y 軸は独立して考えることができる
    xdict = {e: i+1 for i,e in enumerate(sorted(list(set(x))))}
    ydict = {e: i+1 for i,e in enumerate(sorted(list(set(y))))}

    for i in range(n):
        print(f'{xdict[x[i]]} {ydict[y[i]]}')


if __name__ == '__main__':
    run()