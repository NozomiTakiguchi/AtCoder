n = int(input())
a = list(map(int, input().split()))

even  = []
odd = []

for e in a:
    if e %2 == 0:
        even.append(e)
    else:
        odd.append(e)


even = sorted(even, reverse=True)
odd = sorted(odd, reverse=True)

if len(even) < 2:
    if len(odd) < 2:
        print(-1)
        exit()
    ans = sum(odd[:2])
    if ans %2 != 0:
        print(-1)
        exit()
    print(ans)
else:
    ans = sum(even[:2])
    if len(odd) < 2:
        print(ans)
    else:
        print(max([ans, sum(odd[:2])]))
        