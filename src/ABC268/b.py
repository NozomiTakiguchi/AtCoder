s = input()
t = input()

flag = True


if len(s) > len(t):
    print('No')
    exit()

for _s,_t in zip(s,t):
    if _s == _t:
        continue
    else:
        flag = False
        break

if flag:
    print('Yes')
else:
    print('No')