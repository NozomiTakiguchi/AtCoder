n,m = map(int, input().split())
a = list(map(int, input().split()))

s = 0
cnt = 0
start = 0

ans = sum([(i+1)*e if i+1 <= m else 0  for i,e in enumerate(a)])
_s = ans
for i in range(n):

    start = max(i+1-m, 0)
    _a = a[start] # 先頭
    s += a[i]

    if i+1 < m:
        continue

    if i+1 == n:
        break
    _s = _s - s + a[i+1]*(m)
    ans = max(ans, _s)

    if i+1 >= m:
        s -= _a


print(ans)