n,x = map(int, input().split())
pn = list(map(int, input().split()))

for i,p in enumerate(pn):
    if p == x:
        print(i+1)
        exit()