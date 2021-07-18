_n = lambda: int(_i())
_l = lambda: list(map(int, _i().split()))
_i = lambda: input()

def run():
    n = _n()
    a = sorted(_l())
    b = sorted(_l())
    c = sorted(_l())

    ans = 0
    i,j,k = 0,0,0

    while i < n:
        while j < n and b[j] <= a[i]:
            # a[i] より小さな b[j] は使えないため無視する
            j += 1
        if j == n:
            # a < b < c となる組は存在しない 
            break

        while k < n and c[k] <= b[j]:
            # b[j] より小さな c[k] は使えないため無視する
            k += 1
        if k == n:
            # a < b < c となる組は存在しない 
            break
        
        assert a[i] < b[j] < c[k]
        ans += 1
        i,j,k = i+1, j+1, k+1
    
    print(ans)


if __name__ == '__main__':
    run()
