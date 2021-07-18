_n = lambda: int(_i())
_l = lambda: list(map(int, _i().split()))
_i = lambda: input()

def run():
    n = _n()
    s = _i()

    cnt = 0
    for e in s:
        if e == '0':
            cnt += 1
        else:
            break
    print('Takahashi' if cnt%2==0 else 'Aoki')

if __name__ =='__main__':
    run()