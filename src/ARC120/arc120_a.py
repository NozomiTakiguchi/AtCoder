nl = lambda: list(map(int, _i().split()))
_n = lambda: int(_i())
_i = lambda: input()

def run():
    n = _n()
    a = nl()
    s = 0
    t = 0
    m = 0
    for i in range(n):
        s += a[i] # s = a1 + a2 + ... + an
        t += s # t = a1 + (a1+a2) + (a1+a2+a3) + ... + (a1+a2+...+an)
        m = max(m, a[i])
        print(t + m*(i+1))











if __name__ == '__main__':
    run()