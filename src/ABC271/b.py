n,q = map(int, input().split())

l = []
for _ in range(n):
    l.append(list(map(int, input().split())))
st = [(map(int, input().split())) for _ in range(q)]

for e in st:
    s,t = e
    print(l[s-1][t])