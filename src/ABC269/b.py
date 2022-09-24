

s = []
start = False
for i in range(10):
    _s = input()
    s.append([e for e in _s])

a,b,c,d = [0]*4
start = False
for i,e in enumerate(s):
    if '#' in e:
        if not start:
            a = i+1
            start = True
    else:
        if start:
            b = i
            start = False
if start: #最後の行まで埋められている場合
    b = 10

start = False
for j,e in enumerate(s[a-1]):
    if e == '#':
        if not start:
            c = j+1
            start = True
    else:
        if start:
            d = j
            start = False
if start: #最後の列まで埋められている場合
    d = 10

print(a,b)
print(c,d)