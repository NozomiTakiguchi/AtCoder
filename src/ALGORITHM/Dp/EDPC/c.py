ni = lambda: int(_i())
il = lambda: list(map(int, _i().split()))
_i = lambda: input()

# dp は逆算の考え方が大事 ??
# → 後のことも考えて今とるアクションを考慮する必要があるから

def run():
    n = ni()
    l = []
    for _ in range(n):
        l.append(il())
    
    dp = [0 for _ in range(n+1)]

    prev = 0
    for i in range(n):
        if i == 0:
            cnddt = [(e,i) for i,e in enumerate(l[i])]
        else:
            cnddt = [(e,i) for i,e in enumerate(l[i]) if i != prev]
        amt, prev = max(cnddt, key=lambda x: x[0])
        dp[i+1] = dp[i] + amt
    print(dp[n])


if __name__ == '__main__':
    run()