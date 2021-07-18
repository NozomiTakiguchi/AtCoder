_n = lambda: int(_i())
_l = lambda: list(map(int, _i().split()))
_i = lambda: input()

def run():
    n,a,x,y = _l()
    print(a*x + (n-a)*y if n-a >= 0 else n*x)

if __name__ =='__main__':
    run()
