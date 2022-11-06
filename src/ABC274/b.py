h,w = map(int, input().split())
l = []
for _ in range(h):
    _l = []
    s = input()
    for e in s:
        _l.append(e)
    l.append(_l)

ans = [0]*w
for i,e in enumerate(l):
    for j,ee in enumerate(e):
        if ee == '#':
            ans[j] += 1


print(*ans)