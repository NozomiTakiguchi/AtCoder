_n = lambda: int(_i())
_l = lambda: list(map(int, _i().split()))
_i = lambda: input()

MOD = 998244353
def run():
    n,k = _l()

    a = [0] * n
    b = [0] * n
    for i in range(k):
        c,_k = input().split()
        _k = int(_k) - 1
        b[_k] = 1
        for j in range(n):
            if c == 'L' and _k <= j: # 数字 i のうち、最も左に位置する i の位置が _k であるため、それより右にはいくらでも i を書き込むことができる
                a[j] += 1
                continue
            if c == 'R' and _k >= j: # 数字 i のうち、最も右に位置する i の位置が _k であるため、それより左にはいくらでも i を書き込むことができる
                a[j] += 1
                continue
    
    ans = 1
    for i in range(n):
        if not b[i]: # 制約により数字が入っている箇所は除外する
            ans *= a[i]
    
    print(ans%MOD)


if __name__ == '__main__':
    run()