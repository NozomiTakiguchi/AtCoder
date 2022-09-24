a,b = map(int, input().split())
ans = 0


l = []
if a == 0:
    pass
elif a < 3:
    l.append(a)
elif a == 3:
    l.append(1)
    l.append(2)
elif a == 4:
    l.append(a)
elif a == 5:
    l.append(1)
    l.append(4)
elif a == 6:
    l.append(2)
    l.append(4)
else:
    l.append(1)
    l.append(2)
    l.append(4)


if b == 0:
    pass
elif b < 3:
    l.append(b)
elif b == 3:
    l.append(1)
    l.append(2)
elif b == 4:
    l.append(b)
elif b == 5:
    l.append(1)
    l.append(4)
elif b == 6:
    l.append(2)
    l.append(4)
else:
    l.append(1)
    l.append(2)
    l.append(4)

if len(l) == 0:
    print(0)
    exit()
l = list(set(l))
print(sum(l))