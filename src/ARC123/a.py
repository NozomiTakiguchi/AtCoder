_n = lambda: int(_i())
_l = lambda: list(map(int, _i().split()))
_i = lambda: input()

def run():
    a1,a2,a3 = _l()

    if 2*a2 <= a1 + a3:
        if (a1+a3 - 2*a2)%2 != 0:
            print(int(((a1+a3-2*a2+1)/2)+1))
        else:
            print(int((a1+a3-2*a2)/2))

    else:
        print(int(2*a2 - a1-a3))

if __name__ == '__main__':
    run()