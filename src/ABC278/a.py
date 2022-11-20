n,k = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(k):
    a.append(0)

print(*a[k:])